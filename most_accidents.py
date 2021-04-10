"""
@author Austin Cepalia acc5989@rit.edu 
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv')
df = df[pd.to_datetime(df['CRASH DATE']) >= pd.to_datetime('2020-01-01')]
df = df[pd.to_datetime(df['CRASH DATE']) < pd.to_datetime('2021-01-01')]
accident_counts = df['BOROUGH'].value_counts()
accident_counts.plot(kind="bar")

plt.title("Accidents by Borough - 2020")
plt.xlabel("Borough")
plt.ylabel("Number of accidents")
plt.gcf().subplots_adjust(bottom=0.30)
plt.show()


