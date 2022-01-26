import json
import logging
import pathlib
from typing import Optional, List
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI, APIRouter, HTTPException
from starlette.responses import FileResponse
import datetime
from app.util_files import (
    get_feeding_data,
    get_head_data,
    get_height_data,
    get_weight_data,
)
from app.db_utils import get_db_data, update_db_head, update_db_wnh, update_db_feeding
from app.db_setup import reset_fcn

datas = APIRouter()


PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_PATH / "logs/info.log"

favicon_path = PROJECT_PATH / "data/favicon.png"

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
)


@datas.get("/favicon.ico", include_in_schema=False)
async def favicon():
    logging.info("Opened favicon")
    return FileResponse(favicon_path)


@datas.get("/")
async def index_get():
    logging.info("Opened landing page")
    return


# class WeightItem(BaseModel):
#     date: List[datetime.date]
#     week: List[float]
#     weight: List[float]

@datas.get("/weight")
async def weight_data_page():
    logging.info("Opened weight page")
    #result = get_weight_data()
    result = get_db_data("weight")
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Weight data not found")
    
    result = dict(result)
    
    return result


@datas.get("/head")
async def head_data_page():
    logging.info("Opened head circumference page")
    #result = get_head_data()
    result = get_db_data("head")
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Head data not found")
    
    result = dict(result)
    return result


@datas.get("/height")
async def height_data_page():
    logging.info("Opened height page")
    #result = get_height_data()
    result = get_db_data("height")
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Height data not found")
    
    result = dict(result)
    return result


@datas.get("/feeding")
async def feeding():
    logging.info("Opened feeding page")
    #result = get_feeding_data()
    result = get_db_data("feeding")
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Feeding data not found")
    
    result = dict(result)
    return result

@datas.get("/reset_db")
def reset_db():
    reset_fcn()
    return

@datas.post("/wnh_update")
async def update_wnh(date: str, week: float, weight: float, height: float):
    update_db_wnh(date, week, weight, height)
    return 

@datas.post("/head_update")
async def update_head(week: float, head: float):
    update_db_head(week, head)
    return    
    

@datas.post("/feeding_update")
async def update_wnh(date: str, time: str, bm_vol: int, formula_vol: int):
    update_db_feeding(date, time, bm_vol, formula_vol)
    return 

