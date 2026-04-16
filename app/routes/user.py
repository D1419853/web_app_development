from flask import Blueprint, render_template, session, redirect, url_for

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/history')
def history():
    """
    查看個人歷史紀錄。
    需檢查是否已登入。
    """
    # 邏輯預留：session['user_id'], Record.get_by_user_id
    return render_template('history.html')
