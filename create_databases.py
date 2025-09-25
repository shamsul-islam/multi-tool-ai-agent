
import pandas as pd
import sqlite3

def csv_to_sqlite(csv_path, db_path, table_name):
    """
    Converts a CSV file to a SQLite database.
    """
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Successfully converted {csv_path} to {db_path} with table '{table_name}'")

if __name__ == '__main__':
    csv_to_sqlite('heart.csv', 'heart_disease.db', 'heart_disease')
    csv_to_sqlite('cancer.csv', 'cancer.db', 'cancer')
    csv_to_sqlite('diabetes.csv', 'diabetes.db', 'diabetes')
