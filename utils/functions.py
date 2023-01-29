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

from utils.classes import FileDataset


pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', 50)


def exit_analysis(**kwargs):
    """Exits the program."""
    command = kwargs["exit"]
    if command == "exit":
        print("Thanks bye")
        return 1
    else:
        return 0


def read_commands(commands_dict={}):
    """Lists all available default commands and in the Titanic Analysis program"""
    return_dict = {}
    for key in commands_dict:
        return_dict[key] = commands_dict[key].__doc__
    return return_dict


def print_commands(**kwargs):
    """Lists all available default commands and in the Titanic Analysis program"""
    commands_dscr = kwargs["read_commands"](kwargs["commands_dict"])

    print("Command: Short Description")
    for key, value in commands_dscr.items():
        print("{}: {}".format(key, value))


# def cleanup(**kwargs):
#     """Removes unpacked files"""
#     for path in os.listdir(**kwargs):
#         file_name = Path("utils") / "data" / path
#         os.remove(file_name)
#         print("File: {} was removed successfully".format(path))
#

def show_hist(**kwargs):
    """Displays histogram for Age category"""
    obj = FileDataset(**kwargs)
    return obj.scatter()


def init_obj(**kwargs):
    """Displays histogram for Age category"""
    return FileDataset(**kwargs)





