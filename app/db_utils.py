import sqlite3
import pathlib
import pandas as pd

PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_PATH / "app/baby_data.db"

def get_db_data(choose_data):
    global DB_PATH
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        if choose_data == "weight":
            cur.execute("SELECT date, week, weight FROM weight_table;")
            result = cur.fetchall()
            df = pd.DataFrame(result, columns=['date', 'week', 'weight'])
        elif choose_data == "height":
            cur.execute("SELECT week, Height FROM Height_table;")
            result = cur.fetchall()
            df = pd.DataFrame(result, columns=['week', 'height'])
        elif choose_data == "head":
            cur.execute("SELECT week, head FROM head_table;")
            result = cur.fetchall()
            df = pd.DataFrame(result, columns=['week', 'head'])
        elif choose_data == "feeding":
            cur.execute("SELECT date, time, bm_vol, formula_vol FROM feeding_table;")
            result = cur.fetchall()
            df = pd.DataFrame(result, columns=['date', 'time', 'bm_vol', 'formula_vol'])
            df['total_vol'] = df.bm_vol.astype(int) + df.formula_vol.astype(int)
            df["date"] = pd.to_datetime(df["date"], dayfirst=True).dt.date
            df = df.groupby(["date"], as_index=False).sum()
            df = df.astype(str)
        else: df=""
        
        return df


def update_db_head(week, head):
    global DB_PATH
    data_tuple = ((str(week), str(head)))
    
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO head_table (week, head) VALUES (?,?);", data_tuple)
        
def update_db_wnh(date, week, weight, height):
    global DB_PATH
    data_tuple_w = ((str(date), str(week),str(weight)))
    data_tuple_h = ((str(week), str(height)))
    
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO weight_table (date, week, weight) VALUES (?,?,?);", data_tuple_w)
        cur.execute("INSERT INTO height_table (week, height) VALUES (?,?);", data_tuple_h)
        
    return


def update_db_feeding(date, time, bm_vol, formula_vol):
    global DB_PATH
    data_tuple = ((str(date), str(time),str(bm_vol), str(formula_vol)))
    
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO feeding_table (date, time, bm_vol, formula_vol) VALUES (?,?,?,?);", data_tuple)
        
    return

def print_time():
    global DB_PATH
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT time FROM feeding_table;")
        result = cur.fetchall()
        print(result)
    return



# if __name__ == "__main__":
#     print_time()
    
