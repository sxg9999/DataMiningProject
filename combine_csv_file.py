import pandas as pd
import numpy as np


file_name_prefix = "data/Motor_Vehicle_Collisions_-_Crashes_month_"

file_name_arr = [file_name_prefix + str(i) +".csv" for i in range(1, 13)]

output_file = "data/Motor_Vehicle_Collisions_-_Crashes_combined.csv"

df_arr = []

for file_name in file_name_arr:
    df = pd.read_csv(file_name)
    df_arr.append(df)

result = pd.concat(df_arr, ignore_index=True)

result.to_csv(output_file, index=False)



