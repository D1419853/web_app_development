from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if not username or not password:
            flash('請填寫必填欄位')
            return render_template('auth/register.html')
            
        if User.get_by_username(username):
            flash('帳號已存在')
            return render_template('auth/register.html')
            
        hashed_password = generate_password_hash(password)
        User.create(username, hashed_password, email)
        flash('註冊成功，請登入')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.get_by_username(username)
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash(f'歡迎回來, {username}!')
            return redirect(url_for('main.index'))
            
        flash('帳號或密碼錯誤')
        
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('您已登出')
    return redirect(url_for('main.index'))
