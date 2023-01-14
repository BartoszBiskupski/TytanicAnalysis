# from kaggle.api.kaggle_api_extended import KaggleApi
# api = KaggleApi()
# api.authenticate()
#
#
# print(api.competition_download_files('titanic'))
import os
from zipfile import ZipFile
from pathlib import Path
# from classes import FileDataset
#
extract_path = Path("utils") / "data"
zip_path = Path("utils") / "titanic.zip"
# test_path = Path("utils") / "data" / "test.csv"
#
# test_load = FileDataset(file_path="data/train.csv")
# print(test_load.data.head())


def unpack_data(command=""):
    """unpacks source data from the zip file."""
    try:
        zf = ZipFile(zip_path)
        zf.extractall(extract_path) #save files in selected folder
        zf.close()
        print("sucesfully unpaced")
    except Exception():
        print("errrorororoor")


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


