import requests

from ddipy import constants
from ddipy.constants import DATA_NOT_FOUND, MISSING_PARAMETER
from ddipy.ddi_utils import VerifyUtils, BadRequest


class DatabaseClient:

    def __init__(self):
        pass

    @staticmethod
    def get_database_pic(database_name):
        if not database_name:
            raise BadRequest("missing parameter database_name", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.DATABASE_URL + "/" + database_name + "/picture", headers=constants.HEADERS)
        return res

    @staticmethod
    def get_database_all():
        res = requests.get(constants.DATABASE_ALL_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return res

    @staticmethod
    def get_database_db_picturebyte():
        res = requests.get(constants.DATABASE_PICTURE_URL, headers=constants.HEADERS)
        return res
