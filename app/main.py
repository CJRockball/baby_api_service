import json
import logging
import pathlib
from typing import Optional
import pandas as pd

from fastapi import FastAPI, APIRouter, HTTPException
from starlette.responses import FileResponse

from app.util_files import (
    get_feeding_data,
    get_head_data,
    get_height_data,
    get_weight_data,
)

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


@datas.get("/weight")
async def weight_data_page():
    logging.info("Opened weight page")
    result = get_weight_data()
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Weight data not found")
    
    result = dict(result)
    return result


@datas.get("/head")
async def head_data_page():
    logging.info("Opened head circumference page")
    result = get_head_data()
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Head data not found")
    
    result = dict(result)
    return result


@datas.get("/height")
async def height_data_page():
    logging.info("Opened height page")
    result = get_height_data()
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Height data not found")
    
    result = dict(result)
    return result


@datas.get("/feeding")
async def feeding():
    logging.info("Opened feeding page")
    result = get_feeding_data()
    
    if not isinstance(result, pd.DataFrame):
        raise HTTPException(status_code=404, detail="Feeding data not found")
    
    result = dict(result)
    return result

