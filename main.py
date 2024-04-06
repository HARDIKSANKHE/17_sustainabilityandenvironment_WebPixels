import pandas as pd
import os

preset_directory = './Hackathon_data/Grid_data'

def merge_five_years_of_csv(file_prefix, merge_file_name):
    dfs = []

    for filename in os.listdir(preset_directory):
        if filename.startswith(file_prefix) and filename.endswith(".csv"):
            df = pd.read_csv(os.path.join(preset_directory, filename))
            dfs.append(df)

    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv(merge_file_name, index=False)


def merge_all_csv_into_one():
    price_df = pd.read_csv('price_per_unit.csv')
    consumption_df = pd.read_csv('unit_consumption.csv')
    stability_df = pd.read_csv(f'{preset_directory}/grid_stability_2019_2023.csv')

    merged_temp_df = pd.merge(price_df, consumption_df, on='date')

    merged_df = pd.merge(merged_temp_df, stability_df, on='date')

    merged_df = merged_df[['date', 'c1', 'c2', 'c3', 'p1', 'p2', 'p3', 'stability']]

    merged_df.to_csv('grid_stability_5years.csv', index=False)


merge_five_years_of_csv('price_per_unit_', 'price_per_unit.csv')
merge_five_years_of_csv('unit_consumption_', 'unit_consumption.csv')

merge_all_csv_into_one()