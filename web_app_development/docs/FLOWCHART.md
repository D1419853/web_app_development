# 線上占卜系統 — 流程圖設計 (Flowchart)

> **版本：** v1.0
> **建立日期：** 2026-04-09
> **專案名稱：** 線上占卜系統

---

## 1. 使用者流程圖 (User Flow)

描述使用者進入系統後的主要操作路徑。

```mermaid
flowchart TD
    Start([使用者進入網站]) --> Home[首頁 - 每日指引與導覽]
    Home --> Nav{選擇動作}
    
    Nav -->|未登入| Login[登入 / 註冊頁]
    Login --> Auth{驗證成功?}
    Auth -->|是| Profile[個人導覽頁]
    Auth -->|否| Login
    
    Nav -->|前往占卜| FortunePool[占卜中心]
    FortunePool --> Choice{選擇方式}
    Choice -->|抽籤| Draw[線上抽籤筒]
    Choice -->|算命| Calculate[命理資訊輸入]
    Choice -->|擲筊| Toss[虛擬擲筊]
    
    Draw --> Result[顯示籤詩與解籤]
    Calculate --> Result
    Toss --> Result
    
    Result --> Save{儲存紀錄?}
    Save -->|是，且已登入| HistoryDB[存入資料庫]
    Save -->|是，未登入| PromptLogin[提示登入]
    Save -->|否| Home
    
    HistoryDB --> HistoryView[查看歷史紀錄]
    
    Nav -->|展示誠意| Donate[模擬捐香油錢]
    Donate --> FinishDonate[獲得感謝與功德記錄]
    FinishDonate --> Home
```

---

## 2. 系統序列圖 (Sequence Diagram)

以「線上抽籤」為例，描述前端到後端資料庫的完整互動流程。

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器 (Vue/Jinja2)
    participant Flask as Flask Route (/draw)
    participant DB as SQLite (fortune.db)

    User->>Browser: 點擊「開始抽籤」
    Browser->>Flask: POST /api/draw_lot
    Note left of Flask: 產生隨機數點選籤王
    Flask->>DB: SELECT * FROM lots WHERE id = random_id
    DB-->>Flask: 回傳籤詩與白話解釋
    
    alt 已登入
        Flask->>DB: INSERT INTO user_history (user_id, lot_id, type)
        DB-->>Flask: 成功
    end
    
    Flask-->>Browser: 回傳 JSON 結果 (籤詩、解說、動畫指令)
    Browser->>User: 顯示抽籤動畫並展示結果頁面
```

---

## 3. 功能清單與路由對照表

本表列出系統核心功能對應的技術實作路徑。

| 功能名稱 | 說明 | URL 路徑 | 方法 |
| :--- | :--- | :--- | :--- |
| **首頁** | 顯示每日指引與快速入口 | `/` | `GET` |
| **註冊** | 使用者帳號建立 | `/register` | `GET/POST` |
| **登入** | 使用者身份驗證 | `/login` | `GET/POST` |
| **抽籤入口** | 線上抽籤功能頁面 | `/fortune/draw` | `GET/POST` |
| **算命入口** | 八字/姓名算命輸入頁 | `/fortune/calculate` | `GET/POST` |
| **擲筊入口** | 線上擲筊動畫頁面 | `/fortune/toss` | `GET/POST` |
| **歷史紀錄** | 查看個人過去占卜結果 | `/history` | `GET` |
| **模擬捐款** | 捐獻香油錢操作 | `/donate` | `GET/POST` |
| **個人資料** | 修改暱稱與頭像 | `/profile` | `GET/POST` |

---

## 4. 異常處理流程

1. **未登入存取保護頁面**：系統將自動重新導向至 `/login`。
2. **抽籤資料庫異常**：若無法取得籤詩，顯示「神明忙碌中，請稍後再試」提示。
3. **資料輸入錯誤**：算命輸入資訊不完整時，前端進行 JS 攔截並提示。
