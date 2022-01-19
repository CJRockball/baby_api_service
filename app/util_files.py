import pathlib

import pandas as pd


def get_weight_data():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FILE = PROJECT_PATH / "data/weight_data.ods"
    if DATA_FILE.exists():
        try:
            df = pd.read_excel(DATA_FILE)
            df = df.astype(str)
            return df
        except Exception as error:
            print("Couldn't load data", error)
            return ""
    else:
        print("No file found")
        return ""


def get_head_data():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FILE = PROJECT_PATH / "data/head_data.ods"
    
    if DATA_FILE.exists():
        try:
            df = pd.read_excel(DATA_FILE)
            df = df.astype(str)
            return df
        except Exception as error:
            print("Couldn't load data", error)
            return ""
    else:
        print("No file found")
        return ""


def get_height_data():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FILE = PROJECT_PATH / "data/height_data.ods"
    if DATA_FILE.exists():
        try:
            df = pd.read_excel(DATA_FILE)
            df = df.astype(str)
            return df
        except Exception as error:
            print("Couldn't load data", error)
            return ""
    else:
        print("No file found")
        return ""


def get_feeding_data():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FILE = PROJECT_PATH / "data/feeding.ods"
    
    if DATA_FILE.exists():
        try:
            df = pd.read_excel(DATA_FILE)
            df = df.rename(
            columns={"Date": "date", "BM Volume": "bm_vol", "Formula Volume": "formula_vol"}
            )
            df2 = df.copy()

            df2["date"] = pd.to_datetime(df2["date"], dayfirst=True).dt.date
            df2["total_vol"] = df2.bm_vol + df2.formula_vol

            da = df2.groupby(["date"], as_index=False).sum()
            da = da.astype(str)
            return da
        except Exception as error:
            print("Couldn't load data", error)
            return ""
    else:
        print("No file found")
        return ""
    
 
