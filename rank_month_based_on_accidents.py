import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

file_path = "data/Motor_Vehicle_Collisions_-_Crashes_combined.csv"

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

def main():
    dataframe = load_data()
    compute_total_accidents_per_month(dataframe)

    print("Before 2020: ")
    print(total_accident_before_2020)

    print("2020:")
    print(total_accident_2020)
    


if __name__ == "__main__":
    main()
