from app.models import get_db_connection

class Fortune:
    @staticmethod
    def create(type, title, content, image_path=None):
        """
        新增一筆籤詩/占卜結果到資料庫池。
        """
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO fortunes (type, title, content, image_path) VALUES (?, ?, ?, ?)',
                (type, title, content, image_path)
            )
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating fortune: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_all():
        """
        獲取所有籤詩內容。
        """
        conn = get_db_connection()
        fortunes = conn.execute('SELECT * FROM fortunes').fetchall()
        conn.close()
        return fortunes

    @staticmethod
    def get_by_id(fortune_id):
        """
        獲取單筆籤詩。
        """
        conn = get_db_connection()
        fortune = conn.execute('SELECT * FROM fortunes WHERE id = ?', (fortune_id,)).fetchone()
        conn.close()
        return fortune

    @staticmethod
    def get_random(type=None):
        """
        核心邏輯：隨機抽選一筆結果。
        """
        conn = get_db_connection()
        if type:
            fortune = conn.execute(
                'SELECT * FROM fortunes WHERE type = ? ORDER BY RANDOM() LIMIT 1',
                (type,)
            ).fetchone()
        else:
            fortune = conn.execute(
                'SELECT * FROM fortunes ORDER BY RANDOM() LIMIT 1'
            ).fetchone()
        conn.close()
        return fortune

    @staticmethod
    def delete(fortune_id):
        """
        移除籤詩。
        """
        conn = get_db_connection()
        try:
            conn.execute('DELETE FROM fortunes WHERE id = ?', (fortune_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting fortune: {e}")
            return False
        finally:
            conn.close()
