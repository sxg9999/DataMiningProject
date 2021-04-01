"""Parzen Density Estimation
   @authors Christopher Haen cmh6674@rit.edu 
            Steven Guan sxg8944@rit.edu
"""
import pandas
from sklearn.neighbors import KernelDensity
from pandas.core.frame import DataFrame


def parzen_density_estimation(data: DataFrame):
  KernelDensity(kernel='gaussian', bandwidth=0.2).fit(data.to_numpy())


data = pandas.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv')
parzen_density_estimation(data)