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


y_axis_name = 'NUMBER OF PERSONS KILLED'

def clean():
  data = pandas.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv')

  data = data[['ZIP CODE', y_axis_name, 'CRASH TIME']]
  # Reduce rows for testing
  # data = data.head(100000)

  data.dropna(axis=0, inplace=True)

  data['TIMESTAMP'] = data['CRASH TIME'].apply(lambda s: float(s.split(':')[0]) + int(s.split(':')[1]) * (1 / 60))
  data['ZIP CODE'] = pandas.to_numeric(data['ZIP CODE'], errors='coerce', downcast='integer')
  data[y_axis_name] = pandas.to_numeric(data[y_axis_name], errors='coerce', downcast='integer')

  data.dropna(axis=0, inplace=True)

  return data


clean_data = clean()
#two_dim_kde(clean_data.to_numpy())

ax1 = clean_data.plot(kind='scatter', x='TIMESTAMP', y=y_axis_name, label='scatter')
ax1.set_xticks(np.arange(24))
ax2 = clean_data['TIMESTAMP'].plot(kind='kde', color='red', label='kde', secondary_y=True)
ax1.set_ylabel('')
ax2.set_ylabel('KDE')
ax1.legend(loc=1)
ax2.legend(loc=2)
plt.show()
