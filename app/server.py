from fastapi import FastAPI
from app.main import datas

app = FastAPI()

app.include_router(datas, prefix='/api/v1/datas', tags=['datas'])