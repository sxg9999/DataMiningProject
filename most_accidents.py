"""
@author Austin Cepalia acc5989@rit.edu 
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_data_month_8.csv')

accident_counts = df['BOROUGH'].value_counts()
accident_counts.plot(kind="bar")

plt.title("Accidents by Borough - 08/2012")
plt.xlabel("Borough")
plt.ylabel("Number of accidents")
plt.gcf().subplots_adjust(bottom=0.30)
plt.show()


#print(df.BOROUGH.unique())

