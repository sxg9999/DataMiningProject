
import os
import shutil
import math
import pandas as pd
import numpy as np
from datetime import datetime
import global_vars
import time





def get_matched(unknown_str: str, str_list: list):
  """
  return the similarity ratio and the string that is most similar to the unknown_str
  """

  max_similarity = 0
  max_sim_str = ""
  unkn_str_len = len(unknown_str)
  unkn_str_upper = unknown_str.upper()

  # print("unknown string is " + unkn_str_upper)

  for valid_str in str_list:
    # print("valid str is : " + valid_str)
    valid_str_len = len(valid_str)
    # print("valid str length is : " + str(valid_str_len))

    similarity = 0

    if unkn_str_len > valid_str_len:
      diff = unkn_str_len - valid_str_len
      # print("unknown str len is: " + str(unkn_str_len))

      for i in range(0, diff + 1):
        # print("unknown sub str is : " + unkn_str_upper[i:i+valid_str_len])
        similarity = levenshtein_similarity(valid_str.upper(), unkn_str_upper[i:i + valid_str_len])

        if similarity > max_similarity:
          max_similarity = similarity
          max_sim_str = valid_str

        if max_similarity >= .75:
          return max_similarity, max_sim_str

    else:
      similarity = levenshtein_similarity(valid_str.upper(), unkn_str_upper)

      if similarity > max_similarity:
        max_similarity = similarity
        max_sim_str = valid_str

      if max_similarity >= .75:
        return max_similarity, max_sim_str

  return max_similarity, max_sim_str


def levenshtein_similarity(valid_str: str, unknown_str: str):
  """
  Calculates the levenshtein distance between two strings and
  convert that to a similarity ratio

  *Code is referenced from datacamp.com*
  """

  rows = len(valid_str) + 1
  cols = len(unknown_str) + 1
  distance_matrix = np.zeros((rows, cols), dtype=int)

  # populate the distance_matrix with the index of each character of both strings
  for valid_str_index in range(1, rows):
    distance_matrix[valid_str_index][0] = valid_str_index
    for unkn_str_index in range(1, cols):
      distance_matrix[0][unkn_str_index] = unkn_str_index

  # iterate over the matrix to compute the cost of deletions, insertions and/or substitions
  for col in range(1, cols):
    for row in range(1, rows):
      if valid_str[row - 1] == unknown_str[col - 1]:
        cost = 0  # no cost if the two characters are the same
      else:
        cost = 2

      distance_matrix[row][col] = min(distance_matrix[row - 1][col] + 1,  # cost of deletions
                                      distance_matrix[row][col - 1] + 1,  # cost of insertion
                                      distance_matrix[row - 1][col - 1] + cost)  # cost of substitution

  similarity = ((len(valid_str) + len(unknown_str)) - distance_matrix[row][col]) / (len(valid_str) + len(unknown_str))
  # print(distance_matrix)

  return similarity


def get_month_datas(dataframe:pd.DataFrame):
  month = global_vars.month
  month_data_list = []
  num_of_records = len(dataframe)

  for i in range(num_of_records):
    time_str = dataframe.loc[i, 'CRASH DATE']
    date = datetime.strptime(time_str, "%m/%d/%Y")
    if date.month == month:
      month_data_list.append(dataframe.iloc[i])
      print("inserted record_" + str(i) + " month = " + str(month))

  new_data_frame = pd.DataFrame(month_data_list)
  new_data_frame.index = range(len(new_data_frame))

  return new_data_frame


def get_borough_w_lat_long(latitude, longitude):


  borough_lat_long = global_vars.borough_lat_long


  min_lat_diff = math.inf
  min_long_diff = math.inf
  min_borough = ""

  boroughs = global_vars.boroughs

  for borough in boroughs:
    (b_lat, b_long) = borough_lat_long[borough]
    lat_diff = abs(b_lat - latitude)
    long_diff = abs(b_long - longitude)

    if lat_diff < min_lat_diff and long_diff < min_long_diff:
      min_lat_diff = lat_diff
      min_long_diff = long_diff
      min_borough = borough

  return min_borough

def get_borough_str(row: pd.DataFrame, boroughs):
  return_val = "none"

  borough_str = row['BOROUGH']
  if not pd.isna(borough_str):
    max_similarity, max_str = get_matched(borough_str, boroughs)

    if max_similarity >= 0.75:
      return_val = max_str

  return return_val


def add_time_stamp_and_sort(dataframe:pd.DataFrame):
  print("Adding timestamps and sorting ...")
  dataframe['TIMESTAMP'] = pd.to_datetime(dataframe['CRASH DATE'] + " " + dataframe['CRASH TIME'])
  dataframe = dataframe.sort_values(by=['TIMESTAMP'])

  dataframe.index = range(len(dataframe))

  return dataframe


def add_accident_types(dataframe:pd.DataFrame):
  print("Adding accident types ...")
  dataframe['ACCIDENT_TYPE'] = dataframe.apply(lambda row: get_car_accident_type(row), axis=1)
  dataframe = remove_none_accident_type(dataframe)
  dataframe = dataframe.drop(columns=global_vars.drop_cols)
  dataframe.index = range(len(dataframe))
  return dataframe

def remove_none_accident_type(dataframe: pd.DataFrame):
  print("Removing accident type with none values ...")
  num_of_rows = len(dataframe)

  for i in range(num_of_rows):
    val = dataframe.loc[i, 'ACCIDENT_TYPE']
    if val == "none":
      dataframe.drop(index=i, inplace=True)

  return dataframe

def get_car_accident_type(row:pd.DataFrame):
  return_val = "none"

  ppl_killed_injured =  row['NUMBER OF PEDESTRIANS INJURED'] + row['NUMBER OF PEDESTRIANS KILLED'] +\
                        row['NUMBER OF CYCLIST INJURED'] + row['NUMBER OF CYCLIST KILLED'] +\
                        row['NUMBER OF MOTORIST INJURED'] + row['NUMBER OF MOTORIST KILLED']


  vehicle_2_str = row['VEHICLE TYPE CODE 2']

  if ppl_killed_injured > 0:
    return_val = "car-pedestrian"
  elif ppl_killed_injured <= 0:

    if pd.notna(vehicle_2_str):
      max_similarity, max_str = get_matched(vehicle_2_str.lower(), global_vars.pedestrian_vehicles)

      if max_similarity >= 0.75:
        return_val = "car-pedestrian"
      else:
        return_val = "car-only"


  print("result = " + str(return_val))
  return return_val




def verify_borough_cols(dataframe:pd.DataFrame):
  print("Verifying borough cols ...")
  dataframe['BOROUGH'] = dataframe.apply(lambda row: get_borough_str(row, global_vars.boroughs), axis = 1)
  return dataframe



def add_missing_borough(row:pd.DataFrame, def_borough:str, def_lat, def_long):
  if row['BOROUGH'] == "none":
    if pd.isna(row['LATITUDE']) or pd.isna(row['LONGITUDE']) or row['LATITUDE'] == 0 or row['LONGITUDE'] == 0:
      row['BOROUGH'] = def_borough
      row['LATITUDE'] = def_lat
      row['LONGITUDE'] = def_long
    else:
      borough_str = get_borough_w_lat_long(row['LATITUDE'], row['LONGITUDE'])
      row['BOROUGH'] = borough_str

  return row


def fill_in_missing_boroughs(dataframe:pd.DataFrame):
  print("Filling in missing boroughs ...")
  median_lat = dataframe['LATITUDE'].median()
  median_long = dataframe['LONGITUDE'].median()
  def_borough = get_borough_w_lat_long(median_lat, median_long)
  dataframe = dataframe.apply(lambda row : add_missing_borough(row, def_borough, median_lat, median_long), axis=1)

  return dataframe



def save_dataframe(dataframe:pd.DataFrame):
  dataframe.to_csv(global_vars.output_file_path, index=False)

def load_data():
  empty_df = pd.read_csv(global_vars.file_path, nrows=0)
  col_names = list(empty_df.columns)


  df = pd.read_csv(global_vars.file_path, names=col_names, usecols=global_vars.useful_cols, skiprows=1, low_memory=False)

  df = get_month_datas(df)
  df = add_accident_types(df)
  df = verify_borough_cols(df)
  df = fill_in_missing_boroughs(df)
  df = add_time_stamp_and_sort(df)

  save_dataframe(df)

  print(df)

if __name__ == "__main__":

  start = time.time()
  load_data()
  end = time.time()

  print("Time in seconds : ", end-start)
