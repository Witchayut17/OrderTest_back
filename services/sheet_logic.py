from repository.sheet_repo import return_csv_repo
import pandas as pd
import io
from fastapi import UploadFile
from utils.connection import get_conn

sheet = get_conn

def make_column(data: list[dict]) -> list[dict]:
    if not data:
        return []
    new_rows = []
    for row in data:
        max_len = max((len(v) for v in row.values() if isinstance(v, list)),default=1)
        for i in range(max_len):
            new_row = {}
            for key, values in row.items():
                if isinstance(values, list):
                    new_row[key] = values[i] if i < len(values) else ""
                else:
                    new_row[key] = values
            new_rows.append(new_row)
    return new_rows

async def create_csv(data:list[dict], path:str):
    transform = make_column(data)
    if not transform:
        return False
    result = await return_csv_repo(transform, path)
    return result

async def upload_handle(file:UploadFile):
    df = pd.read_csv(io.StringIO((await file.read()).decode("utf-8")))
    sheet.update([df.columns.values.tolist()] + df.values.tolist())
    return df