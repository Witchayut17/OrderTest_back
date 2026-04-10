import gspread
from oauth2client.service_account import ServiceAccountCredentials
import motor.motor_asyncio
from setting import MONGO_DB
import json

def get_conn():
    scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]

    creds_json = os.getenv("credentials")
    creds_dict = json.loads(creds_json)
    cred = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(cred)
    spreadsheet = client.open("TestPandas")
    sheet = spreadsheet.sheet1
    return sheet

def get_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
    db = client.Company
    return db