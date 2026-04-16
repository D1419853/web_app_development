import os
from flask import Flask
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

def create_app():
    """
    建立並配置 Flask 應用程式。
    """
    app = Flask(__name__)
    
    # 配置
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # 延遲匯入以避免循環導入
    from app.routes import register_blueprints
    register_blueprints(app)
    
    return app
