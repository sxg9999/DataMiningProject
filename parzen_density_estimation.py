"""Parzen Density Estimation
   @authors Christopher Haen cmh6674@rit.edu 
            Steven Guan sxg8944@rit.edu
"""
import numpy as np
import pandas
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn
from sklearn.neighbors import KernelDensity
from pandas.core.frame import DataFrame
from scipy.stats import gaussian_kde
from matplotlib.pyplot import imread

###################
# KDE ZIP VS TIME #
###################
y_axis_name = 'NUMBER OF PERSONS KILLED'

def zip_clean():
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

def plot_zip_code():
  clean_data = zip_clean()
  #two_dim_kde(clean_data.to_numpy())

  ax1 = clean_data.plot(kind='scatter', x='TIMESTAMP', y=y_axis_name, label='scatter')
  ax1.set_xticks(np.arange(24))
  ax2 = clean_data['TIMESTAMP'].plot(kind='kde', color='red', label='kde', secondary_y=True)
  ax1.set_ylabel('')
  ax2.set_ylabel('KDE')
  ax1.legend(loc=1)
  ax2.legend(loc=2)
  plt.show()

# plot_zip_code()


###############
# KDE HEATMAP #
###############
def heatmap_clean(data: DataFrame, t1 = pandas.Timestamp.min, t2 = pandas.Timestamp.now()):
  data.dropna(axis=0, inplace=True)
  data = data[(data['TIMESTAMP'].map(pandas.Timestamp) >= t1) & (data['TIMESTAMP'].map(pandas.Timestamp) < t2)]

  print('Before', len(data))
  # Filter out coordinates outside city
  # https://boundingbox.klokantech.com/
  data = data[(data['LATITUDE'] != 0) & (data['LATITUDE'] >= 39) & (data['LATITUDE'] <= 41)]
  data = data[(data['LONGITUDE'] != 0) & (data['LONGITUDE'] >= -74.3) & (data['LONGITUDE'] <= -70)]
  print('After', len(data))

  return data


def heatmap(data: DataFrame, t1 = pandas.Timestamp.min, t2 = pandas.Timestamp.now()):
  data = heatmap_clean(data, t1, t2)
  seaborn.kdeplot(
    data=data, x="LONGITUDE", y="LATITUDE", hue="BOROUGH", levels=6,
  )

  t1_str = str(t1.year) + '/' + str(t1.month) + '/' + str(t1.day)
  t2_str = str(t2.year) + '/' + str(t2.month) + '/' + str(t2.day)
  plt.title('Accidents by Type: ' + t1_str + ' - ' + t2_str)
  plt.show()


file = 'DataMiningProject\data\Crash Data\Motor_Vehicle_Collisions_-_Crashes_combined.csv'
file = 'DataMiningProject\data\cleaned_data_month_8.csv'
#file = 'DataMiningProject\data\month_8_short_TEST_ONLY.csv'
data = pandas.read_csv(file)

#heatmap(data, pandas.Timestamp.min, pandas.Timestamp(2020, 1, 1))
#heatmap(data, pandas.Timestamp(2020, 1, 1), pandas.Timestamp(2021, 1, 1))


def open_streets(data: DataFrame, t1 = pandas.Timestamp.min, t2 = pandas.Timestamp.now()):
  data = heatmap_clean(data, t1, t2)
  data = data[data['ACCIDENT_TYPE'] == 'car-pedestrian']
  ax1 = seaborn.kdeplot(
    data=data, x="LONGITUDE", y="LATITUDE", hue="BOROUGH", alpha=0.6
  )

  ax2 = seaborn.scatterplot(data=data, x='LONGITUDE', y='LATITUDE', s=4, alpha=0.5)

  t1_str = str(t1.year) + '/' + str(t1.month) + '/' + str(t1.day)
  t2_str = str(t2.year) + '/' + str(t2.month) + '/' + str(t2.day)
  plt.title('Accidents by Type: ' + t1_str + ' - ' + t2_str)
  
  img = imread('DataMiningProject\\data\\Charts\\new-york-city-maps.jpg')
  ax1.imshow(img, zorder=-1, extent=[-74.25, -73.7, 40.48, 40.92])

  plt.show()


# open_streets(data, pandas.Timestamp(2020, 1, 1), pandas.Timestamp(2021, 1, 1))