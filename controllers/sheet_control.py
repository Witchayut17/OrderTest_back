from services.sheet_logic import create_csv, upload_handle
from fastapi import HTTPException, UploadFile, File, Request
from models.sheet_model import CsvInput, OrderPayload
import time
import pandas as pd
from repository.sheet_repo import mongo_insert_repo, mongo_dataframe_repo , mongo_food_insert_repo, mongo_food_get_repo

async def create_csv_control(data:CsvInput):
    try:
        start = time.time()
        result = await create_csv(data.data, f"{data.sheet.name}.csv")
        end = time.time()
        response = end - start
        return {"Status":f"Sucessfully create csv file in local {response} sec"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
async def upload_csv_control(file: UploadFile = File(...)):
    try:
        start = time.time()
        result = await upload_handle(file)
        end = time.time()
        response = end - start
        return {"Status":f"Sucessfully upload csv file from local to google spreadsheet {response} sec"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
async def mongo_insert_control():
    try:
        result = await mongo_insert_repo()
        return {"Status":"Sucessfully insert data from sheet to mongodb"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
async def mongo_read_control(filename=""):
    try:
        df = await mongo_dataframe_repo()
        df.to_csv(f"{filename}.csv", index=False)
        return {"Status":"Sucessfully export csv from mongo"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
async def mongo_food_insert_control(order:OrderPayload):
    try:
        result = await mongo_food_insert_repo(order.data)
        return {"Status":"Sucessfully received data from BOTNOI SME PLATFORM"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
async def mongo_food_get_control():
    try:
        result = await mongo_food_get_repo()
        return result
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))