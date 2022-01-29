from fastapi import FastAPI
from app.main import datas
from app.db_web import up_data

app = FastAPI()

app.include_router(datas, prefix='/api/v1/datas', tags=['datas'])
app.include_router(up_data, prefix='/api/v1/up_data', tags=['up_data'])