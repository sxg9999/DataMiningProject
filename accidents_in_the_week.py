#
# Accident by week visuals (only for August)
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



file_path = "data/Motor_Vehicle_Collisions_-_Crashes_month_8.csv"


accident_dict = {}

week_day_dict = {
    "Monday": 0,
    "Tuesday":1,
    "Wednesday":2,
    "Thursday":3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}


def compute_avg_accidents_before_2020():
    years =  list(accident_dict.keys())
    accident_dict['< 2020'] = [0,0,0,0,0,0,0]

    count = 0

    print(years)
    for year in years:
        if year != '2020':
            count += 1
            print("add year : ", year)
            for i in range(7):
                
                accident_dict['< 2020'][i] += accident_dict[year][i]

    print(count)
    for i in range(7):
        accident_count = accident_dict['< 2020'][i]
        accident_dict['< 2020'][i] = accident_count/count

def compute_avg_accidents_per_weekday(dataframe: pd.DataFrame):
    num_of_records = len(dataframe)

    for i in range(num_of_records):
        year = str(dataframe['year'][i])
        weekday_str = dataframe['day_of_week'][i]
        weekday_int = week_day_dict[weekday_str]
        accident_dict[year][weekday_int] += 1
    
    # normalize the count of accidents by week by dividing it by the number of weeks per year
    weeks_per_year = 4

    years = accident_dict.keys()
    for year in years:
        for i in range(7):
            accident_count = accident_dict[year][i]
            normalized_count = accident_count/weeks_per_year
            accident_dict[year][i] = round(normalized_count)
        print(accident_dict[year])



def init_accident_dict():
    global accident_dict

    for i in range(2012, 2021):
        accident_dict[str(i)] = [0,0,0,0,0,0,0]


def graph():
    before_2020 = accident_dict['< 2020']
    on_2020 = accident_dict['2020']
    week_days = ["Mon", "Tues", "Weds", "Thurs", "Fri", "Sat", "Sun"]

    df = pd.DataFrame({'< 2020': before_2020, '2020': on_2020}, index = week_days)
    ax = df.plot.bar(rot=0,  title="Accidents by Weekday")
    ax.set_xlabel("Weekdays")
    ax.set_ylabel("Number of Car Accidents (Car-only, Car-Pedestrian)")
    
    plt.show()

def load_data():
    dataframe = pd.read_csv(file_path, parse_dates=['TIMESTAMP'])
    dataframe['day_of_week'] = dataframe['TIMESTAMP'].dt.day_name()
    dataframe['year'] = dataframe['TIMESTAMP'].dt.year


    # dataframe['day_of_week'].plot.bar()
    # plt.show()

    print(dataframe)
    return dataframe

def main():
    dataframe = load_data()
    init_accident_dict()
    compute_avg_accidents_per_weekday(dataframe)
    compute_avg_accidents_before_2020()
    print(accident_dict)
    print(week_day_dict)
    print(accident_dict)
    graph()
    # compute_avg_accidents_per_weekday(dataframe)
    


if __name__ == "__main__":
    main()