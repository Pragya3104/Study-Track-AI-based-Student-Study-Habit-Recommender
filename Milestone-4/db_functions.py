import mysql.connector
import pandas as pd

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # Add your MySQL root password here
        database="study_tracker"
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS study_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id VARCHAR(50),
        subject VARCHAR(100),
        topic VARCHAR(255),
        duration INT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_log(student_id, subject, topic, duration):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO study_logs (student_id, subject, topic, duration) VALUES (%s,%s,%s,%s)",
        (student_id, subject, topic, duration)
    )
    conn.commit()
    cursor.close()
    conn.close()

def fetch_logs(student_id):
    conn = get_connection()
    df = pd.read_sql(
        "SELECT * FROM study_logs WHERE student_id = %s",
        conn,
        params=(student_id,)
    )
    conn.close()
    return df

def fetch_all():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM study_logs", conn)
    conn.close()
    return df

def update_log(record_id, new_duration):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE study_logs SET duration = %s WHERE id = %s",
        (new_duration, record_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_log(record_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM study_logs WHERE id = %s",
        (record_id,)
    )
    conn.commit()
    cursor.close()
    conn.close()
