import pandas as pd
import os
import predictions

if(not os.path.exists("./csv")):
    os.mkdir("./csv")

if(not os.path.exists("./csv/final")):
    os.mkdir("./csv/final")

def merge_five_years_of_csv(file_prefix, merge_file_name, preset_directory):
    dfs = []

    for filename in os.listdir(preset_directory):
        if filename.startswith(file_prefix) and filename.endswith(".csv"):
            df = pd.read_csv(os.path.join(preset_directory, filename))
            dfs.append(df)

        if filename.startswith(file_prefix) and filename.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(preset_directory, filename))
            dfs.append(df)

    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv(merge_file_name, index=False)


def merge_csv_into_one():
    grid_data_preset_directory = "./Hackathon_data/Grid_data"
    merge_five_years_of_csv('price_per_unit_', 'csv/price_per_unit.csv', grid_data_preset_directory)
    merge_five_years_of_csv('unit_consumption_', 'csv/unit_consumption.csv', grid_data_preset_directory)

    price_df = pd.read_csv('csv/price_per_unit.csv')
    consumption_df = pd.read_csv('csv/unit_consumption.csv')
    stability_df = pd.read_csv(f'{grid_data_preset_directory}/grid_stability_2019_2023.csv')

    merged_temp_df = pd.merge(price_df, consumption_df, on='date')

    merged_df = pd.merge(merged_temp_df, stability_df, on='date')

    merged_df = merged_df[['date', 'c1', 'c2', 'c3', 'p1', 'p2', 'p3', 'stability']]

    merged_df.to_csv('csv/final/grid_stability_5years.csv', index=False)


def merge_excel_into_one():
    wind_power_data_preset_directory = "./Hackathon_data/wind_power_data"
    merge_five_years_of_csv('air_temperature_', 'csv/air_temperature.csv', wind_power_data_preset_directory)
    merge_five_years_of_csv('power_gen_', 'csv/power_gen.csv', wind_power_data_preset_directory)
    merge_five_years_of_csv('pressure_', 'csv/pressure.csv', wind_power_data_preset_directory)
    merge_five_years_of_csv('wind_speed_', 'csv/wind_speed.csv', wind_power_data_preset_directory)

    validation_data_df = pd.read_excel (f"{wind_power_data_preset_directory}/wind_power_gen_3months_validation_data.xlsx")
    validation_data_df.rename(columns={
        'DateTime': 'date',
        'Air temperature | (°C)': 'air_temperature',
        'Pressure | (atm)': 'pressure',
        'Power generated by system | (MW)': 'power_generated_by_system',
        'Wind speed | (m/s)': 'wind_speed',
        }, inplace=True)
    validation_data_df.to_csv ("csv/final/wind_power_gen_3months_validation_data.csv", index = None, header=True)

    air_temperature_df = pd.read_csv('csv/air_temperature.csv')
    power_gen_df = pd.read_csv('csv/power_gen.csv')
    pressure_df = pd.read_csv('csv/pressure.csv')
    wind_speed_df = pd.read_csv('csv/wind_speed.csv')

    merge_on = "DateTime"
    merged_df = pd.merge(air_temperature_df, power_gen_df, on=merge_on)
    merged_df = pd.merge(merged_df, pressure_df, on=merge_on)
    merged_df = pd.merge(merged_df, wind_speed_df, on=merge_on)

    merged_df.rename(columns={
        'DateTime': 'date',
        'Air temperature | (°C)': 'air_temperature',
        'Pressure | (atm)': 'pressure',
        'Power generated by system | (MW)': 'power_generated_by_system',
        'Wind speed | (m/s)': 'wind_speed',
        }, inplace=True)
    
    merged_df = merged_df[['date', 'air_temperature', 'pressure', 'wind_speed', 'power_generated_by_system']]

    merged_df.to_csv('csv/final/wind_power_gen_5years.csv', index=False)



merge_csv_into_one()
merge_excel_into_one()

predictions.get_total_power_generated()