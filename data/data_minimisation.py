import pandas as pd
import numpy as np


class Cleaning:

    def open_data(self):
        """ iport csv file either by absolut path, either by relative path
        """
        df = pd.read_csv(r'/home/imad/Becode/Projects/Challeng-NYC-New/data/data_100000.csv')
        # df = pd.read_csv("data_100000.csv")

        return df

    def add_day_month_columns(self, df):
        """ divid the crash data columns to three columns
        """
        df["crash_date"] = df["crash_date"].astype(str)
        df['day'] = df['crash_date'].apply(lambda day: day[8:10])
        df['month'] = df['crash_date'].apply(lambda day: day[5:7])
        df['year'] = df['crash_date'].apply(lambda day: day[0:4])
        df["day"] = df["day"].astype(int)
        df["month"] = df["month"].astype(int)
        df["year"] = df["year"].astype(int)
        #df[["crash_date","day", "month", "year"]].head()
        return df

    def delet_unnecessary_columns(self, df):
        """
        remove crashe_data, latitude, longitude, columns because we divided crashe_data to three columns and latitude, longitude, are reapeted columns
        """
        df = df.drop(["crash_date", "borough", "zip_code", "latitude", "longitude","on_street_name", "off_street_name", "cross_street_name"], axis=1)
        return df

    def drop_null_value(self, df):
        """
        remova all columns that has null values > 90000
        """
        df = df.drop(
            df.columns[df.apply(lambda col: col.isnull().sum() > 90000)], axis=1)

        return df

    def replace_Nan_by_necessary_value(self, df):
        """
        replace all nan value in contributing_factor_vehicle_1 and contributing_factor_vehicle_2 and ..... to unspecified
        """
        df['contributing_factor_vehicle_1'] = df['contributing_factor_vehicle_1'].fillna("Unspecified")
        df['contributing_factor_vehicle_2'] = df['contributing_factor_vehicle_2'].fillna("Unspecified")
        df['vehicle_type_code1'] = df['vehicle_type_code1'].fillna("Unspecified")
        df['vehicle_type_code2'] = df['vehicle_type_code2'].fillna("Unspecified")
        return df

    def replace_injured_killed_columns(self, df):
        """
        replace all injured coliumns by one columns called person_injured
        """
        df["number_of_person_injured"] = df["number_of_persons_injured"] + df["number_of_pedestrians_injured"] + df["number_of_motorist_injured"]+ df["number_of_persons_injured"]
        df["number_of_person_killed"] = df["number_of_persons_killed"] + df["number_of_pedestrians_killed"] + df["number_of_motorist_killed"]+ df["number_of_persons_killed"]
        df = df.drop(['number_of_persons_injured', 'number_of_persons_killed',
        'number_of_pedestrians_injured', 'number_of_pedestrians_killed',
        'number_of_cyclist_injured', 'number_of_cyclist_killed',
        'number_of_motorist_injured', 'number_of_motorist_killed'], axis=1)
        return df

    def injured_killed_columns_normalized(self, df):
        """
        replace all killed coliumns by one columns called person_killed
        """
        df["number_of_person_injured"] = (df["number_of_person_injured"] - df["number_of_person_injured"].min()) / (
            df["number_of_person_injured"].max() - df["number_of_person_injured"].min())
        df["number_of_person_killed"] = (df["number_of_person_killed"] - df["number_of_person_killed"].min()) / (
            df["number_of_person_killed"].max() - df["number_of_person_killed"].min())
        return df

    def tranfert_to_str(self, df):
        df["location"] = df["location"].str.strip("()")
        df["location"] = df["location"].astype(str)
        df = df[['crash_time', 'day', 'month', 'year', 'location', 'contributing_factor_vehicle_1','contributing_factor_vehicle_2', 'collision_id', 'vehicle_type_code1','vehicle_type_code2','number_of_person_injured', 'number_of_person_killed']]

        return df

    def creat_csv_file(self, df):
        """ creat a csv file to write into the cleaned data
        """
        cleaned_data = df.to_csv("hard_cleaned_data.csv", index = False, header=True)
        return cleaned_data


df = Cleaning().open_data()
df = Cleaning().add_day_month_columns(df)
df = Cleaning().delet_unnecessary_columns(df)
df = Cleaning().drop_null_value(df)
df = Cleaning().replace_Nan_by_necessary_value(df)
df = Cleaning().replace_injured_killed_columns(df)
df = Cleaning().injured_killed_columns_normalized(df)
df = Cleaning().tranfert_to_str(df)
df = Cleaning().creat_csv_file(df)
# print(df.head(), df.shape)
# print(df.info())
