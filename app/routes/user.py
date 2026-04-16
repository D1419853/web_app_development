from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models.record import Record

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/history')
def history():
    if 'user_id' not in session:
        flash('請先登入以查看歷史紀錄')
        return redirect(url_for('auth.login'))
        
    records = Record.get_by_user_id(session['user_id'])
    return render_template('history.html', records=records)
