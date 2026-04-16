from app.routes.main import main_bp
from app.routes.auth import auth_bp
from app.routes.user import user_bp

def register_blueprints(app):
    """
    註冊所有的 Flask Blueprints。
    """
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
