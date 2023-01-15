# from kaggle.api.kaggle_api_extended import KaggleApi
# api = KaggleApi()
# api.authenticate()
#
#
# print(api.competition_download_files('titanic'))
import os
from zipfile import ZipFile
from pathlib import Path
import pandas as pd
from tabulate import tabulate
from utils.classes import FileDataset
from utils.classes import DataVisualizer

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', 50)
#
extract_path = Path("utils") / "data"
zip_path = Path("utils") / "titanic.zip"
# test_path = Path("utils") / "data" / "train.csv"

#print(tabulate(test_load.data.head(100), headers="keys", tablefmt="psql"))




def unpack_data(command=""):
    """unpacks source data from the zip file."""
    try:
        zf = ZipFile(zip_path)
        zf.extractall(extract_path) #save files in selected folder
        zf.close()
        print("Successfully unpacked all files")
    except Exception():
        print("Something went wrong")


def exit_analysis(command=""):
    """Exits the program."""
    if command == "exit":
        print("Thanks bye")
        return 1
    else:
        return 0


def read_commands(command="", commands_dict={}):
    """Lists all available default commands and in the Titanic Analysis program"""
    return_dict = {}
    for key in commands_dict:
        return_dict[key] = commands_dict[key].__doc__
    return return_dict


def cleanup(command=""):
    """Removes unpacked files"""
    for path in os.listdir(extract_path):
        file_name = Path("utils") / "data" / path
        os.remove(file_name)
        print("File: {} was removed successfully".format(path))


def display_table(command=""):
    """Displays all data in a table format"""
    test_load = FileDataset(file_path="utils/data/train.csv")
    print(tabulate(test_load.data.head(100), headers="keys", tablefmt="psql"))


def return_table(command=""):
    test_load = FileDataset(file_path="utils/data/train.csv")
    return test_load.data


def display_hist(df, command=""):
    test_scatter = DataVisualizer(df)
    print(test_scatter.scatter())





