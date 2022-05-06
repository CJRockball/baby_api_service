import sqlite3
import pandas as pd
import pathlib


PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_PATH / "app/baby_data.db"

def setup_db():
    global DB_PATH
    # Connect to db
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # Create a table
    cur.execute("""DROP TABLE IF EXISTS weight_table""")
    cur.execute("""DROP TABLE IF EXISTS height_table""")
    cur.execute("""DROP TABLE IF EXISTS head_table""")
    cur.execute("""DROP TABLE IF EXISTS feeding_table""")
    
    cur.execute(
        """CREATE TABLE IF NOT EXISTS weight_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    week TEXT,
                    weight TEXT);"""
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS height_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    week TEXT,
                    height TEXT);"""
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS head_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    week TEXT,
                    head TEXT);"""
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS feeding_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    time TEXT,
                    bm_vol TEXT,
                    formula_vol TEXT);"""
    )
     
    cur.execute(
        """CREATE TABLE IF NOT EXISTS sleep_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    wake TEXT,
                    sleep TEXT);"""
    )   
    # Write changes
    conn.commit()
    conn.close()
    
    return

def data_insert(data_tuple, command_code):
    global DB_PATH
    # Create a table
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        for entry in data_tuple:
            cur.execute(command_code,entry)

    return

def tuplefy(fname):
    PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
    DATA_FILE = PROJECT_PATH / "data" / fname
    
    if DATA_FILE.exists():
        try:
            df = pd.read_excel(DATA_FILE)
            df = df.astype(str)
            weight_tuple = [tuple(x) for x in df.to_numpy()]
            return weight_tuple
        except Exception as error:
            print("Couldn't load data", error)
            return ""
    else:
        print("No file found")
        return ""


def reset_fcn():
    setup_db()
    
    weight_tuple = tuplefy("weight_data.ods")
    height_tuple = tuplefy("height_data.ods")
    head_tuple = tuplefy("head_data.ods")
    feeding_tuple = tuplefy("feeding.ods")
    sleep_tuple = tuplefy("wake_data.ods")        
        
    data_insert(weight_tuple, "INSERT OR IGNORE INTO weight_table (date, week, weight) VALUES (?,?,?);" "")
    data_insert(height_tuple, "INSERT OR IGNORE INTO height_table (week, height) VALUES (?,?);" "")
    data_insert(head_tuple, "INSERT OR IGNORE INTO head_table (week, head) VALUES (?,?);" "")
    data_insert(feeding_tuple, "INSERT OR IGNORE INTO feeding_table (date, time, bm_vol, formula_vol) VALUES (?,?,?,?);" "")
    data_insert(sleep_tuple, "INSERT OR IGNORE INTO sleep_table (date, wake, sleep) VALUES (?,?,?);" "")

    return


if __name__ == "__main__":
    setup_db()
    
    weight_tuple = tuplefy("weight_data.ods")
    height_tuple = tuplefy("height_data.ods")
    head_tuple = tuplefy("head_data.ods")
    feeding_tuple = tuplefy("feeding.ods")
    sleep_tuple = tuplefy("wake_data.ods")        
        
    data_insert(weight_tuple, "INSERT OR IGNORE INTO weight_table (date, week, weight) VALUES (?,?,?);" "")
    data_insert(height_tuple, "INSERT OR IGNORE INTO height_table (week, height) VALUES (?,?);" "")
    data_insert(head_tuple, "INSERT OR IGNORE INTO head_table (week, head) VALUES (?,?);" "")
    data_insert(feeding_tuple, "INSERT OR IGNORE INTO feeding_table (date, time, bm_vol, formula_vol) VALUES (?,?,?,?);" "")
    data_insert(sleep_tuple, "INSERT OR IGNORE INTO sleep_table (date, wake, sleep) VALUES (?,?,?);" "")


