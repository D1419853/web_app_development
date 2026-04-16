from app.models import init_db
from app.models.fortune import Fortune

def seed_data():
    print("--- 正在初始化資料庫並植入種子資料 ---")
    init_db()
    
    fortunes = [
        {
            "type": "籤詩",
            "title": "第一籤：大吉",
            "content": "【籤詩內容】\n雲開月出正分明，不須進退問前程。\n婚姻皆老皆圓滿，財源廣進利息增。\n\n【解籤】\n目前正處於運勢上升期。一切疑慮皆會消散，目標清晰可見。不論是求財或感情，皆能得到圓滿的結果。",
            "image_path": None
        },
        {
            "type": "籤詩",
            "title": "第二籤：上吉",
            "content": "【籤詩內容】\n龍吟虎嘯出山林，威震乾坤動地心。\n萬里鵬程從此始，名高利厚遂初襟。\n\n【解籤】\n這是一個事業大顯身手的好時機。正如龍吟虎嘯，您的才華即將被世人看見，前途無量。",
            "image_path": None
        },
        {
            "type": "籤詩",
            "title": "第三籤：中平",
            "content": "【籤詩內容】\n凡事必須守舊章，不可妄動傷陰功。\n雖然目前難遂意，守得雲開見月明。\n\n【解籤】\n現在並非衝動行事的時機。建議守住現狀，不要輕易變動。只要心存正念，等待時機成熟，自然會有轉機。",
            "image_path": None
        },
        {
            "type": "籤詩",
            "title": "第四籤：下下",
            "content": "【籤詩內容】\n路遠山高水又深，行程坎坷費苦心。\n不如退步歸家去，免遭災殃及此身。\n\n【解籤】\n目前的環境極其險惡，強行前進只會損失慘重。建議暫停計畫，回頭檢視基礎，以免陷入更深的困局。",
            "image_path": None
        }
    ]
    
    for f in fortunes:
        Fortune.create(f["type"], f["title"], f["content"], f["image_path"])
        
    print(f"成功植入 {len(fortunes)} 筆籤詩資料。")

if __name__ == "__main__":
    seed_data()
