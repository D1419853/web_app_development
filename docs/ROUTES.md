# 路由設計文件：線上算命系統

本文件規劃了系統的所有 URL 路徑、對應的 HTTP 方法、處理邏輯以及 Jinja2 模板。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| **首頁** | GET | `/` | `index.html` | 顯示導覽與開始按鈕 |
| **註冊頁面** | GET | `/auth/register` | `auth/register.html` | 顯示註冊表單 |
| **處理註冊** | POST | `/auth/register` | — | 建立帳號並重導向至登入 |
| **登入頁面** | GET | `/auth/login` | `auth/login.html` | 顯示登入表單 |
| **處理登入** | POST | `/auth/login` | — | 驗證並重導向至首頁 |
| **登出** | GET | `/auth/logout` | — | 清除 Session 並重導向 |
| **執行抽籤** | POST | `/fortune/draw` | — | 隨機產生結果並重導向至結果頁 |
| **顯示結果** | GET | `/fortune/result/<id>` | `result.html` | 顯示特定 ID 的結果 |
| **儲存結果** | POST | `/fortune/save` | — | 將當前結果存入 user 的歷史紀錄 |
| **歷史紀錄** | GET | `/user/history` | `history.html` | 顯示該使用者的所有紀錄 |
| **捐香油錢頁** | GET | `/fortune/donate` | `donate.html` | 顯示捐款資訊與表單 |
| **處理捐款** | POST | `/fortune/donate` | — | 紀錄金額並重導向 |

## 2. 詳細設計說明

### 2.1 身份驗證 (auth)
- 採用 Flask Session 紀錄登入狀態。
- 密碼儲存前需使用雜湊運算。

### 2.2 算命與抽籤 (fortune)
- `/draw` 邏輯：
    1. 從 `fortunes` 資料表隨機選取一筆。
    2. 如果已登入，可選擇直接存入或等到結果頁再存。
    3. 重導向至 `/result/<id>` 以便分享 URL。
- `/save` 邏輯：
    1. 從表單或 Session 獲取剛產出的結果內容。
    2. 呼叫 `Record.create` 存入資料庫。

## 3. Jinja2 模板清單

所有模板皆繼承自 `app/templates/base.html`。

- `base.html`: 包含標頭 (導覽列) 與頁尾。
- `index.html`: 形象頁面與「求籤」大按鈕。
- `result.html`: 顯示籤詩內容與圖片。
- `auth/login.html`: 登入表單。
- `auth/register.html`: 註冊表單。
- `history.html`: 以清單或卡片顯示過去的紀錄。
- `donate.html`: 包含轉帳帳號或模擬支付按鈕。

## 4. 目錄結構規劃

- `app/routes/auth.py`: 處理登入、註冊。
- `app/routes/main.py`: 處理首頁、抽籤、結果、捐款。
- `app/routes/user.py`: 處理歷史紀錄。
