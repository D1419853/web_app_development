from flask import Blueprint, render_template, request, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    系統首頁。
    """
    return render_template('index.html')

@main_bp.route('/fortune/draw', methods=['POST'])
def draw():
    """
    執行抽籤/算命邏輯。
    隨機挑選結果並重導向。
    """
    # 邏輯預留：從 Fortune Model 隨機取資料
    # result_id = ...
    return redirect(url_for('main.result', result_id=1))

@main_bp.route('/fortune/result/<int:result_id>')
def result(result_id):
    """
    顯示特定的抽籤結果。
    """
    # 邏輯預留：根據 ID 向 DB 查詢結果詳細資料
    return render_template('result.html')

@main_bp.route('/fortune/donate', methods=['GET', 'POST'])
def donate():
    """
    捐獻香油錢。
    GET: 顯示捐獻資訊。
    POST: 接收捐獻表單。
    """
    # 邏輯預留：寫入 Donation DB
    return render_template('donate.html')

@main_bp.route('/fortune/save', methods=['POST'])
def save_record():
    """
    儲存當前的算命結果到個人紀錄。
    """
    # 邏輯預留：檢查登入，呼叫 Record.create
    return redirect(url_for('user.history'))
