from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.fortune import Fortune
from app.models.record import Record, Donation

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/fortune/draw', methods=['POST'])
def draw():
    # 邏輯：隨機抽取一筆結果
    # 可以指定類型，若無則隨機
    fortune_type = request.form.get('type')
    fortune = Fortune.get_random(fortune_type)
    
    if not fortune:
        # 如果池子是空的，建立一個預設的作為保險
        Fortune.create("籤詩", "大吉", "心誠則靈，萬事如意", "/static/images/default.jpg")
        fortune = Fortune.get_random()

    return redirect(url_for('main.result', result_id=fortune['id']))

@main_bp.route('/fortune/result/<int:result_id>')
def result(result_id):
    fortune = Fortune.get_by_id(result_id)
    if not fortune:
        flash('找不到該結果')
        return redirect(url_for('main.index'))
    return render_template('result.html', fortune=fortune)

@main_bp.route('/fortune/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        amount = request.form.get('amount')
        message = request.form.get('message')
        user_id = session.get('user_id')
        
        if not amount:
            flash('請輸入捐獻金額')
            return render_template('donate.html')
            
        Donation.create(user_id, int(amount), message)
        flash('感謝您的慷慨捐獻，功德無量！')
        return redirect(url_for('main.index'))
        
    return render_template('donate.html')

@main_bp.route('/fortune/save', methods=['POST'])
def save_record():
    if 'user_id' not in session:
        flash('請先登入後再儲存紀錄')
        return redirect(url_for('auth.login'))
        
    fortune_id = request.form.get('fortune_id')
    fortune = Fortune.get_by_id(fortune_id)
    
    if fortune:
        Record.create(
            session['user_id'],
            fortune['type'],
            fortune['title'],
            fortune['content']
        )
        flash('紀錄已成功存入您的帳號')
    
    return redirect(url_for('user.history'))
