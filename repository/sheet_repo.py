import io
import aiofiles
import csv
from pathlib import Path
from utils.connection import get_db
from services.sheet_clean import clean_data
import pandas as pd
import json
from datetime import datetime

db = get_db()

async def return_csv_repo(data:list[dict], path:str):
    if not data:
        return None
    header = []
    for row in data:
        for key in row.keys():
            if key not in header:
                header.append(key)
    for row in data:
        for key in header:
            row.setdefault(key, "")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
    async with aiofiles.open(path, 'w', newline='', encoding='utf-8') as f:
        await f.write(output.getvalue())
    return path

async def mongo_insert_repo():
    data = await clean_data()
    result = await db.users.insert_many(data)
    return result

async def mongo_dataframe_repo():
    cursor = db.users.find()
    users = await cursor.to_list(length=100)
    for user in users:
        user["_id"] = str(user["_id"])
    df = pd.DataFrame(users)
    return df

async def mongo_food_insert_repo(data:dict):
    if isinstance(data, list):
        data = data[0]

    if hasattr(data, "model_dump"):
        data = data.model_dump()
    data["created_at"] = datetime.utcnow()
    result = await db.customers.insert_one(data)
    return result

async def mongo_food_get_repo():
    cursor = db.customers.find()
    data = await cursor.to_list(length=100)
    for customer in data:
        customer["_id"] = str(customer["_id"])
    return data