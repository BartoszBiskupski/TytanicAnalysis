# from kaggle.api.kaggle_api_extended import KaggleApi
# api = KaggleApi()
# api.authenticate()
#
#
# print(api.competition_download_files('titanic'))

from zipfile import ZipFile


def unpack_data():
#unpacks source data from the zip file
    try:
        zf = ZipFile(r'source_code/titanic.zip')
        zf.extractall(r'source_code/data/') #save files in selected folder
        zf.close()
    except Exception():
        print("errrorororoor")
