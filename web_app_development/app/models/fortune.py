# app/models/fortune.py
from datetime import datetime

class FortuneItem:
    def __init__(self, id=None, type=None, title=None, verse=None, interpretation=None, category=None):
        self.id = id
        self.type = type
        self.title = title
        self.verse = verse
        self.interpretation = interpretation
        self.category = category

    @staticmethod
    def from_row(row):
        if not row:
            return None
        return FortuneItem(
            id=row['id'],
            type=row['type'],
            title=row['title'],
            verse=row['verse'],
            interpretation=row['interpretation'],
            category=row['category']
        )

class FortuneRecord:
    def __init__(self, id=None, user_id=None, item_id=None, type=None, result_text=None, created_at=None):
        self.id = id
        self.user_id = user_id
        self.item_id = item_id
        self.type = type
        self.result_text = result_text
        self.created_at = created_at or datetime.now().isoformat()

class Donation:
    def __init__(self, id=None, user_id=None, amount=None, message=None, created_at=None):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.message = message
        self.created_at = created_at or datetime.now().isoformat()
