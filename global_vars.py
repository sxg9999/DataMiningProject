

file_path ="Motor_Vehicle_Collisions_-_Crashes.csv"
output_file_path = "data/Motor_Vehicle_Collisions_-_Crashes_month_2.csv"
# file_path = "data/small_data.csv"
# output_file_path = "data/small_data_cleaned.csv"

max_year = 2020
month = 2

useful_cols = ['CRASH DATE', 'CRASH TIME', 'BOROUGH', 'LATITUDE', 'LONGITUDE',
               'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
               'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED', 'NUMBER OF CYCLIST KILLED',
               'NUMBER OF MOTORIST INJURED', 'NUMBER OF MOTORIST KILLED', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2']

drop_cols = [ 'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
               'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED', 'NUMBER OF CYCLIST KILLED',
               'NUMBER OF MOTORIST INJURED', 'NUMBER OF MOTORIST KILLED', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2']

boroughs = ["BRONX", "BROOKLYN", "MANHATTAN", "QUEENS", "STATEN ISLAND"]
borough_lat_long = {
    "BRONX":(40.8448, -73.8648),
    "BROOKLYN":(40.6782, -73.9442),
    "MANHATTAN":(40.7831, -73.9712),
    "QUEENS":(40.7282, -737949),
    "STATEN ISLAND":(40.5795, -74.1502)
  }


pedestrian_vehicles = ['bike', 'bicycle', 'cycle', 'motor', 'motorcycle', 'motorbike']                     # vehicles that indicates a accident involving a pedestrian.

