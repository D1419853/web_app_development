# app/models/user.py
from datetime import datetime

class User:
    def __init__(self, id=None, username=None, password_hash=None, nickname=None, email=None, created_at=None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.nickname = nickname
        self.email = email
        self.created_at = created_at or datetime.now().isoformat()

    @staticmethod
    def from_row(row):
        if not row:
            return None
        return User(
            id=row['id'],
            username=row['username'],
            password_hash=row['password_hash'],
            nickname=row['nickname'],
            email=row['email'],
            created_at=row['created_at']
        )

    # 這裡預留 CRUD 方法的框架，後續實作時會與 db 連結
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
            "email": self.email,
            "created_at": self.created_at
        }
