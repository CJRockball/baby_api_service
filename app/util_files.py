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


def get_feeding_data():
    # df = pd.read_csv("C:/Users/PatCa/Documents/PythonScripts/baby_data/feeding.csv")
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FOLDER = PROJECT_PATH / "data"
    df = pd.read_excel(DATA_FOLDER / "feeding.ods")
    df = df.rename(
        columns={"Date": "date", "BM Volume": "bm_vol", "Formula Volume": "formula_vol"}
    )
    df2 = df.copy()

    df2["date"] = pd.to_datetime(df2["date"], dayfirst=True).dt.date
    df2["total_vol"] = df2.bm_vol + df2.formula_vol

    da = df2.groupby(["date"], as_index=False).sum()

    return da

