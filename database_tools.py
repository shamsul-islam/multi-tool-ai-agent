
import sqlite3

def query_heart_disease_db(query):
    """
    Queries the heart disease database.
    """
    conn = sqlite3.connect('heart_disease.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return str(results)

def query_cancer_db(query):
    """
    Queries the cancer database.
    """
    conn = sqlite3.connect('cancer.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return str(results)

def query_diabetes_db(query):
    """
    Queries the diabetes database.
    """
    conn = sqlite3.connect('diabetes.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return str(results)

