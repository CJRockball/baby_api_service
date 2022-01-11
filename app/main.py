import json
import logging
import pathlib
from typing import Optional

from fastapi import FastAPI
from starlette.responses import FileResponse

from app.util_files import get_weight_data

app = FastAPI()
favicon_path = "favicon.ico"

PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_PATH / "logs/info.log"

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
)


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    logging.info("Opened favicon")
    return FileResponse(favicon_path)


@app.get("/")
def index_get():
    logging.info("Opened landing page")
    return


@app.get("/weight")
def weight_plot():
    logging.info("Opened weight page")
    result = get_weight_data()
    result = dict(result)
    return result
