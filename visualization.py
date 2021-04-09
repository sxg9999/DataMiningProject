"""Visualization Methods
   @author Christopher Haen cmh6674@rit.edu 
"""
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

  plt.bar(unique_types, percents)
  plt.xlabel('Accident Type')
  plt.ylabel('Percent of Occurrences')
  plt.title('Accidents by Type: ' + t1_str + ' - ' + t2_str)
  plt.show()


data = pandas.read_csv('data/cleaned_data_month_8.csv')
accident_type_vs_time(data, pandas.Timestamp.min, pandas.Timestamp(2020, 1, 1))
accident_type_vs_time(data, pandas.Timestamp(2020, 1, 1), pandas.Timestamp(2021, 1, 1))