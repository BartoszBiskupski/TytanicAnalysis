# from kaggle.api.kaggle_api_extended import KaggleApi
# api = KaggleApi()
# api.authenticate()
#
#
# print(api.competition_download_files('titanic'))

from zipfile import ZipFile
from pathlib import Path

extract_path = Path("utils") / "data"
zip_path = Path("utils") / "titanic.zip"
def unpack_data():
#unpacks source data from the zip file
    try:
        zf = ZipFile(zip_path)
        zf.extractall(extract_path) #save files in selected folder
        zf.close()
        print("sucesfully unpaced")
    except Exception():
        print("errrorororoor")
