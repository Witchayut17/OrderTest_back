from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # test first
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# import routers AFTER middleware
from routes import sheet_route
app.include_router(sheet_route.router)