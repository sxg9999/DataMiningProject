#
# Accident by month visuals
# 
# Warning: this takes a minute or two to run
#
# @author: Steven Guan
#


import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime



file_path = "Motor_Vehicle_Collisions_-_Crashes_combined.csv"

total_accident_before_2020 = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0,
}

total_accident_2020 = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0,
}

def compute_total_accidents_per_month(dataframe: pd.DataFrame):
    num_of_records = len(dataframe)

    for i in range(num_of_records):
        month = dataframe['month'][i]
        if dataframe['year'][i] == 2020:
            total_accident_2020[month] += 1
        elif dataframe['year'][i] < 2020:
            total_accident_before_2020[month] += 1

    keys = total_accident_before_2020.keys()
    for key in keys:
        num_of_accidents = total_accident_before_2020[key]
        total_accident_before_2020[key] = num_of_accidents/7



def load_data():
    dataframe = pd.read_csv(file_path, parse_dates=['TIMESTAMP'])
    dataframe['month'] = dataframe['TIMESTAMP'].dt.month
    dataframe['year'] = dataframe['TIMESTAMP'].dt.year


    # dataframe['day_of_week'].plot.bar()
    # plt.show()

    print(dataframe)
    return dataframe


def graph():
    
    before_2020_list = []
    keys = total_accident_before_2020.keys()
    for key in keys:
        before_2020_list.append(total_accident_before_2020[key])
    
    
    on_2020_list = []
    keys = total_accident_2020
    for key in keys:
        on_2020_list.append(total_accident_2020[key])


    month_str = ["Jan", "Feb", "March", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df = pd.DataFrame({'< 2020': before_2020_list, '2020':on_2020_list}, index = month_str)
    ax = df.plot.bar(rot=0,  title="Accidents by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Car Accidents (Car-only, Car-Pedestrian)")

    plt.show()

def main():
    dataframe = load_data()
    compute_total_accidents_per_month(dataframe)

    print("Before 2020: ")
    print(total_accident_before_2020)

    print("2020:")
    print(total_accident_2020)

    graph()
    


if __name__ == "__main__":
    main()