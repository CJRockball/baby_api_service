from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_home(q: Optional[str] = None):
    return {"input": q}

