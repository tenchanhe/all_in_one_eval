import pandas as pd

def parquet_to_csv(parquet_file_path, csv_file_path):
    # 讀取 Parquet 文件
    df = pd.read_parquet(parquet_file_path)
    
    # 將 DataFrame 保存為 CSV 文件
    df.to_csv(csv_file_path, index=False)
    print(f"File converted: {parquet_file_path} to {csv_file_path}")

# 使用範例
parquet_file_path = "dev-00000-of-00001.parquet"
csv_file_path = "dev-00000-of-00001.csv"
parquet_to_csv(parquet_file_path, csv_file_path)
