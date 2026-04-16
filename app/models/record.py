from app.models import get_db_connection

class Record:
    @staticmethod
    def create(user_id, type, result_title, result_content):
        """
        儲存一筆算命/抽籤紀錄。
        """
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO records (user_id, type, result_title, result_content) VALUES (?, ?, ?, ?)',
                (user_id, type, result_title, result_content)
            )
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating record: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_all():
        """
        獲取所有紀錄 (通常用於後台或管理)。
        """
        conn = get_db_connection()
        records = conn.execute('SELECT * FROM records ORDER BY created_at DESC').fetchall()
        conn.close()
        return records

    @staticmethod
    def get_by_id(record_id):
        """
        獲取單筆紀錄詳情。
        """
        conn = get_db_connection()
        record = conn.execute('SELECT * FROM records WHERE id = ?', (record_id,)).fetchone()
        conn.close()
        return record

    @staticmethod
    def get_by_user_id(user_id):
        """
        獲取特定使用者的所有紀錄。
        """
        conn = get_db_connection()
        records = conn.execute(
            'SELECT * FROM records WHERE user_id = ? ORDER BY created_at DESC',
            (user_id,)
        ).fetchall()
        conn.close()
        return records

    @staticmethod
    def delete(record_id):
        """
        刪除紀錄。
        """
        conn = get_db_connection()
        try:
            conn.execute('DELETE FROM records WHERE id = ?', (record_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting record: {e}")
            return False
        finally:
            conn.close()

class Donation:
    @staticmethod
    def create(user_id, amount, message=None):
        """
        新增一筆香油錢捐獻紀錄。
        """
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO donations (user_id, amount, message) VALUES (?, ?, ?)',
                (user_id, amount, message)
            )
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating donation: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_all():
        """
        獲取所有捐獻紀錄。
        """
        conn = get_db_connection()
        donations = conn.execute('SELECT * FROM donations ORDER BY created_at DESC').fetchall()
        conn.close()
        return donations
