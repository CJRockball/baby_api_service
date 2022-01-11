import pathlib

import pandas as pd


def get_weight_data():
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FOLDER = PROJECT_PATH / "data"
    df = pd.read_excel(DATA_FOLDER / "weight_data.ods")
    # result = df.to_json()
    return df

