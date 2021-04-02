"""Parzen Density Estimation
   @authors Christopher Haen cmh6674@rit.edu 
            Steven Guan sxg8944@rit.edu
"""
import numpy as np
import pandas
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.neighbors import KernelDensity
from pandas.core.frame import DataFrame
from scipy.stats import gaussian_kde


def clean():
  data = pandas.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv')

  data = data[['ZIP CODE', 'NUMBER OF PERSONS INJURED']]
  # Reduce rows for testing
  data = data.head(100000)

  data.dropna(axis=0, inplace=True)
  data['ZIP CODE'] = pandas.to_numeric(data['ZIP CODE'], errors='coerce', downcast='integer')
  data['NUMBER OF PERSONS INJURED'] = pandas.to_numeric(data['NUMBER OF PERSONS INJURED'], errors='coerce', downcast='integer')
  data.dropna(axis=0, inplace=True)

  return data


def one_dim_kde(data):
  data.plot.kde()
  plt.show()


def two_dim_kde(data: np.ndarray):
  rvs = data
  rvs = np.append(stats.norm.rvs(loc=2,scale=1,size=(2000,1)),
                stats.norm.rvs(loc=0,scale=3,size=(2000,1)),
                axis=1)
  kde = gaussian_kde(rvs.T)

  # Regular grid to evaluate kde upon
  x_flat = np.r_[rvs[:,0].min():rvs[:,0].max():128j]
  y_flat = np.r_[rvs[:,1].min():rvs[:,1].max():128j]
  x,y = np.meshgrid(x_flat,y_flat)
  grid_coords = np.append(x.reshape(-1,1),y.reshape(-1,1),axis=1)

  z = kde(grid_coords.T)
  z = z.reshape(128,128)

  plt.imshow(z,aspect=x_flat.ptp()/y_flat.ptp())
  plt.show()



clean_data = clean()
#one_dim_kde(clean_data['NUMBER OF PERSONS INJURED'])
#two_dim_kde(clean_data.to_numpy())

ax1 = clean_data.plot(kind='scatter', x='NUMBER OF PERSONS INJURED', y='ZIP CODE', label='scatter')
ax2 = clean_data['NUMBER OF PERSONS INJURED'].plot(kind='kde', color='red', label='kde', secondary_y=True)
ax1.set_ylabel('')
ax2.set_ylabel('KDE')
ax1.legend(loc=1)
ax2.legend(loc=2)
plt.show()
