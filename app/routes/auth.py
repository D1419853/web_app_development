from flask import Blueprint, render_template, request, redirect, url_for, session

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    註冊新使用者。
    GET: 顯示註冊表單。
    POST: 處理註冊邏輯。
    """
    # 邏輯預留：解析表單、檢查重複、密碼雜湊、存入 DB
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    使用者登入。
    GET: 顯示登入表單。
    POST: 驗證帳密並寫入 Session。
    """
    # 邏輯預留：驗證帳密、設定 session['user_id']
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    """
    使用者登出。
    清除 Session 並重導向至首頁。
    """
    # 邏輯預留：session.clear()
    return redirect(url_for('main.index'))
