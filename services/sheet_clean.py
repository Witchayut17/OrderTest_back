from utils.connection import get_conn
import pandas as pd
sheet = get_conn()

async def clean_data():
    data = sheet.get_all_values()
    if not data:
        return {"Status":"Error spreadsheet is empty"}
    df = pd.DataFrame(data[1:], columns=data[0])
    df.replace("", pd.NA, inplace=True)
    df = df.dropna()
    df = df.astype({
        "Email":"string",
        "Name":"string",
        "Age":"int",
        "Phone":"string",
        "Status":"string"
    })
    df["Created_at"] = pd.to_datetime(df["Created_at"], errors='coerce')
    df_age = df[df["Age"] > 18]
    df_age = df_age.reset_index(drop=True)
    df_unique = df_age.drop_duplicates(subset="Email", keep="first")
    return df_unique.to_dict(orient='records')