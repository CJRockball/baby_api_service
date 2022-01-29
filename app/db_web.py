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

up_data = APIRouter()


PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_PATH / "logs/info.log"

favicon_path = PROJECT_PATH / "data/favicon.png"

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
)



@up_data.get("/reset_db")
def reset_db():
    reset_fcn()
    logging.info("Reset function")
    return

@up_data.post("/wnh_update")
async def update_wnh(date: str, week: float, weight: float, height: float):
    update_db_wnh(date, week, weight, height)
    logging.info("Ran wnh update function")
    return 

@up_data.post("/head_update")
async def update_head(week: float, head: float):
    update_db_head(week, head)
    logging.info("Ran head update function")
    return    
    

@up_data.post("/feeding_update")
async def update_wnh(date: str, time: str, bm_vol: int, formula_vol: int):
    update_db_feeding(date, time, bm_vol, formula_vol)
    logging.info("Ran feeding update function")
    return 