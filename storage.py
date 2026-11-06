import json
import os

# データ保存用ファイル
DATA_FILE = "data/stocks.json"


# データを保存する関数
def save_stocks(stock_list):

    # 保存先フォルダがなければ作成
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(stock_list, file, ensure_ascii=False, indent=4)


# データを読み込む関数
def load_stocks():

    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)