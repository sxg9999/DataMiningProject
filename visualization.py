"""Visualization Methods
   @author Christopher Haen cmh6674@rit.edu 
"""
import numpy as np
import pandas
import matplotlib.pyplot as plt
from datetime import datetime, time
from pandas.core.frame import DataFrame


def accident_type_vs_time(data: DataFrame, t1 = pandas.Timestamp.min, t2 = pandas.Timestamp.now()):
  unique_types = data['ACCIDENT_TYPE'].unique()
  time_constrained_data = data[(data['TIMESTAMP'].map(pandas.Timestamp) >= t1) & (data['TIMESTAMP'].map(pandas.Timestamp) < t2)]
  accident_type_series = time_constrained_data['ACCIDENT_TYPE']
  percents = []

  for accident_type in unique_types:
    percents.append(len(accident_type_series[accident_type_series == accident_type]) / len(accident_type_series) * 100)

  t1_str = str(t1.year) + '/' + str(t1.month) + '/' + str(t1.day)
  t2_str = str(t2.year) + '/' + str(t2.month) + '/' + str(t2.day)

  print(percents)

  #plt.bar(unique_types, percents)
  plt.pie(percents, labels=unique_types, shadow=True, autopct='%1.1f%%')
  #plt.xlabel('Accident Type')
  #plt.ylabel('Percent of Occurrences')
  plt.title('Accidents by Type: ' + t1_str + ' - ' + t2_str)
  plt.show()


def vehicle_types(data: DataFrame,):
  unique_types = data['VEHICLE TYPE CODE 1'].unique()
  vehicle_type_series = data['VEHICLE TYPE CODE 1']

  types = []
  percents = []

  other = 0
  for vehicle_type in unique_types:
    percent = len(vehicle_type_series[vehicle_type_series == vehicle_type]) / len(vehicle_type_series) * 100
    if percent < 0.75:
      other += percent
    else:
      types.append(vehicle_type)
      percents.append(len(vehicle_type_series[vehicle_type_series == vehicle_type]) / len(vehicle_type_series) * 100)

  types.append('Other')
  percents.append(other)

  combined = zip(percents, types)
  combined = sorted(combined, key = lambda x: x[0])
  combined = list(zip(*combined))

  plt.pie(combined[0], labels=combined[1], shadow=True, autopct='%1.1f%%')
  plt.title('Car Types in Accidents - Less than .75% is grouped in Other')
  plt.show()



#file = 'DataMiningProject\data\Crash Data\Motor_Vehicle_Collisions_-_Crashes_combined.csv'
file = 'DataMiningProject\data\Motor_Vehicle_Collisions_-_Crashes.csv'
# file = 'DataMiningProject\data\cleaned_data_month_8.csv'
data = pandas.read_csv(file)
#accident_type_vs_time(data, pandas.Timestamp.min, pandas.Timestamp(2020, 1, 1))
#accident_type_vs_time(data, pandas.Timestamp(2020, 1, 1), pandas.Timestamp(2021, 1, 1))
vehicle_types(data)