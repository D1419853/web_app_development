import sqlite3
import os

# 資料庫檔案路徑 (存放在 instance/ 目錄下)
DB_PATH = os.path.join('instance', 'database.db')

def get_db_connection():
    """
    建立並回傳 SQLite 資料庫連線。
    """
    # 確保 instance 目錄存在
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    # 使查詢結果可以透過欄位名稱存取 (例如 row['username'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db(schema_path='database/schema.sql'):
    """
    根據 schema.sql 初始化資料庫。
    """
    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found at {schema_path}")
        return

    conn = get_db_connection()
    with open(schema_path, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database initialized successfully.")
