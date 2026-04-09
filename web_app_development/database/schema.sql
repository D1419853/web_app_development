-- 線上占卜系統 資料庫 Schema (SQLite)

-- 1. 使用者資料表
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nickname VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 2. 籤詩/占卜項目資料表 (靜態庫)
CREATE TABLE IF NOT EXISTS fortune_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(20) NOT NULL, -- Lot (抽籤), Divination (算命), Toss (擲筊)
    title VARCHAR(100) NOT NULL, -- 籤號或標題
    verse TEXT NOT NULL,         -- 籤詩原文
    interpretation TEXT NOT NULL, -- 解籤白話
    category VARCHAR(20)          -- 類別 (整體, 感情, 事業, 財運)
);

-- 3. 個人占卜紀錄資料表
CREATE TABLE IF NOT EXISTS fortune_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    item_id INTEGER, -- 可為 NULL (如果是自訂輸入計算的算命)
    type VARCHAR(20) NOT NULL,
    result_text TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES fortune_items(id) ON DELETE SET NULL
);

-- 4. 虛擬捐獻/功德箱紀錄
CREATE TABLE IF NOT EXISTS donations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount FLOAT NOT NULL,
    message TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 5. 初始資料範例 (抽籤項目)
INSERT INTO fortune_items (type, title, verse, interpretation, category)
VALUES 
('Lot', '第一籤 大吉', '福如東海長流水，壽比南山不老松。', '這是極好的預兆，代表萬事亨通，福壽雙全。', '整體'),
('Lot', '第二籤 中平', '平生正直無私曲，問事求謀總有成。', '只要保持正直的心，所求之事終能成辦。', '整體'),
('Toss', '聖筊', '神明降旨，此路通達。', '這代表神明同意你的請求，可以放心去做。', '整體');
