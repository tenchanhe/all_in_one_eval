import pandas as pd
import os
import json

def parquet_to_csv_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".parquet"):
            parquet_file_path = os.path.join(folder_path, file_name)
            csv_file_name = file_name.replace(".parquet", ".csv")
            csv_file_path = os.path.join("./data/mmlu_csv" , csv_file_name)
            
            df = pd.read_parquet(parquet_file_path)

            df.to_csv(csv_file_path, index=True)
            print(f"File converted: {parquet_file_path} to {csv_file_path}")


folder_path = "./data/mmlu_parquet"  
parquet_to_csv_folder(folder_path)

# df = pd.read_parquet('./data/mmlu_parquet/abstract_algebra.parquet')
# print(type(df["choices"]))
# print(df["choices"])