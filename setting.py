import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DB = os.getenv("MONGO_DB")
if not MONGO_DB:
    raise ValueError("Error Can't connected to database")