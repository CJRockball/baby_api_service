import logging
import pathlib
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_PATH / "logs/info.log"

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
)


@app.get("/")
def index_get():
    logging.info("Opened landing page")
    return "Landing Page"

