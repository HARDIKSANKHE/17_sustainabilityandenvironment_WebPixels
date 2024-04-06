import pandas as pd
import zipfile

zip_file_path = 'Hackathon_data.zip'

final_df = pd.DataFrame()

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    for file_name in zip_ref.namelist():
        if file_name.endswith('.csv'):
            df = pd.read_csv(zip_ref.open(file_name))            
            final_df = pd.concat([final_df, df], axis=1)

print(final_df)
