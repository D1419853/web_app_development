from app.models import get_db_connection

class User:
    @staticmethod
    def create(username, password_hash, email=None):
        """
        建立新使用者。
        """
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)',
                (username, password_hash, email)
            )
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_all():
        """
        獲取所有使用者列表。
        """
        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        return users

    @staticmethod
    def get_by_id(user_id):
        """
        透過 ID 獲取使用者資料。
        """
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def get_by_username(username):
        """
        透過使用者名稱獲取資料。
        """
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def update(user_id, data):
        """
        更新使用者資料。
        data: 包含要更新的欄位與值的字典 (如 {'email': 'new@mail.com'})
        """
        if not data:
            return False
            
        conn = get_db_connection()
        try:
            # 動態產生 SQL 語句
            keys = [f"{k} = ?" for k in data.keys()]
            values = list(data.values())
            values.append(user_id)
            
            sql = f"UPDATE users SET {', '.join(keys)} WHERE id = ?"
            conn.execute(sql, values)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def delete(user_id):
        """
        刪除使用者。
        """
        conn = get_db_connection()
        try:
            conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            conn.close()
