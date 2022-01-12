import pathlib

import pandas as pd


def get_weight_data():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FOLDER = PROJECT_PATH / "data"
    df = pd.read_excel(DATA_FOLDER / "weight_data.ods")
    return df


def get_head_data():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FOLDER = PROJECT_PATH / "data"
    df = pd.read_excel(DATA_FOLDER / "head_data.ods")
    df["week"] = df.week.astype(float)
    return df


def get_height_data():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FOLDER = PROJECT_PATH / "data"
    df = pd.read_excel(DATA_FOLDER / "height_data.ods")
    df["week"] = df.week.astype(float)
    return df
