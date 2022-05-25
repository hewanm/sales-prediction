import pandas as pd
import pickle
import dvc.api
from time import gmtime, strftime
from logger import App_Logger

class FileHandler():

    def __init__(self):
        # self.logger = App_Logger().get_logger(__name__)
        pass

    def to_csv(self, df, csv_path, index=False):
        try:
            df.to_csv(csv_path, index=index)
            # self.logger.info(f'Csv file saved in {csv_path}.')

        except Exception:
            self.logger.exception('File saving failed.')

    def read_csv(self, csv_path, missing_values=["n/a", "na", "undefined"]):
        try:
            df = pd.read_csv(csv_path, na_values=missing_values)
            # self.logger.info(f'Csv file read from {csv_path}.')
            return df

        except FileNotFoundError:
            # self.logger.exception('File not found.')
            pass

#     def get_data_url_from_dvc(self, file_path, version):
#         try:
#             data_url = dvc.api.get_url(path=str(file_path), repo=str(Config.REPO), rev=version)
#             # self.logger.info("Data url fetched from dvc.")
#             return df

#         except Exception:
#             # self.logger.exception("Error while fetching data url from dvc.")
#             pass