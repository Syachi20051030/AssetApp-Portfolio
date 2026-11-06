from storage import save_stocks, load_stocks
# =========================
# 資産管理アプリ AssetApp
# =========================

# 保有銘柄データ
stocks = load_stocks()


# =========================
# 計算処理
# =========================

def calculate_total(shares, price):
    """株数と株価から合計金額を計算する"""
    return shares * price


def calculate_stock_data(stock):
    """銘柄ごとの購入総額・評価額・損益を計算する"""
    purchase_total = calculate_total(
        stock["shares"], stock["price"]
    )
    current_value = calculate_total(
        stock["shares"], stock["current_price"]
    )

    profit = current_value - purchase_total
    profit_rate = profit / purchase_total * 100

    return purchase_total, current_value, profit, profit_rate


def calculate_total_current_value(stock_list):
    """保有銘柄全体の現在評価額を計算する"""
    return sum(
        calculate_total(stock["shares"], stock["current_price"])
        for stock in stock_list
    )


def calculate_total_dividend(stock_list):
    """年間配当金の合計を計算する"""
    return sum(
        stock["dividend"] * stock["shares"]
        for stock in stock_list
    )


# =========================
# 入力処理
# =========================

def input_positive_int(message):
    """正の整数を入力する"""
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("1以上の数値を入力してください")
        except ValueError:
            print("整数を入力してください")


def input_positive_float(message, allow_zero=False):
    """正の小数または0を入力する"""
    while True:
        try:
            value = float(input(message))

            if value > 0 or (allow_zero and value == 0):
                return value

            print("正しい数値を入力してください")

        except ValueError:
            print("数値を入力してください")


# =========================
# 銘柄登録
# =========================

def register_stock(stock_list):
    """新しい銘柄を登録する"""

    while True:
        name = input("銘柄名を入力してください：").strip()

        if not name:
            print("銘柄名を入力してください")
            continue

        shares = input_positive_int("保有株数：")
        price = input_positive_float("購入価格：")
        current_price = input_positive_float("現在価格：")
        dividend = input_positive_float(
            "一株あたり年間配当金：", allow_zero=True
        )

        stock = {
            "name": name,
            "shares": shares,
            "price": price,
            "current_price": current_price,
            "dividend": dividend
        }

        stock_list.append(stock)

        save_stocks(stock_list)

        print(f"{name}を登録しました")

        answer = input("追加で登録しますか？ yes/no：").strip().lower()

        if answer == "no":
            break


# =========================
# 保有銘柄一覧
# =========================

def show_stocks(stock_list):
    """保有銘柄とポートフォリオ全体を表示する"""

    if not stock_list:
        print("銘柄が登録されていません")
        return

    total_assets = 0
    current_assets = 0
    total_dividend = 0

    print("\n==== 保有銘柄一覧 ====")

    for stock in stock_list:
        purchase_total, current_value, profit, profit_rate = (
            calculate_stock_data(stock)
        )

        annual_dividend = stock["dividend"] * stock["shares"]

        print(f"\n銘柄：{stock['name']}")
        print(f"株数：{stock['shares']:,}株")
        print(f"購入価格：{stock['price']:,.1f}円")
        print(f"現在価格：{stock['current_price']:,.1f}円")
        print(f"購入総額：{purchase_total:,.1f}円")
        print(f"現在評価額：{current_value:,.1f}円")
        print(f"評価損益：{profit:+,.1f}円")
        print(f"評価損益率：{profit_rate:+.2f}%")
        print(f"年間配当金：{annual_dividend:,.1f}円")

        yield_rate = stock["dividend"] / stock["price"] * 100
        print(f"取得価格ベース配当利回り：{yield_rate:.2f}%")

        total_assets += purchase_total
        current_assets += current_value
        total_dividend += annual_dividend

    total_profit = current_assets - total_assets
    total_profit_rate = total_profit / total_assets * 100
    total_yield = total_dividend / total_assets * 100

    print("\n==== ポートフォリオ全体 ====")
    print(f"投資総額：{total_assets:,.1f}円")
    print(f"現在評価額：{current_assets:,.1f}円")
    print(f"評価損益合計：{total_profit:+,.1f}円")
    print(f"評価損益率合計：{total_profit_rate:+.2f}%")
    print(f"年間配当金合計：{total_dividend:,.1f}円")
    print(f"取得価格ベース配当利回り：{total_yield:.2f}%")


# =========================
# 評価損益ランキング
# =========================

def show_ranking(stock_list):
    """評価損益と評価損益率のランキングを表示する"""

    if not stock_list:
        print("銘柄が登録されていません")
        return

    profit_ranking = sorted(
        stock_list,
        key=lambda stock: calculate_stock_data(stock)[2],
        reverse=True
    )

    profit_rate_ranking = sorted(
        stock_list,
        key=lambda stock: calculate_stock_data(stock)[3],
        reverse=True
    )

    print("\n==== 評価損益ランキング ====")

    for rank, stock in enumerate(profit_ranking, start=1):
        profit = calculate_stock_data(stock)[2]
        print(f"{rank}位：{stock['name']} {profit:+,.0f}円")

    print("\n==== 評価損益率ランキング ====")

    for rank, stock in enumerate(profit_rate_ranking, start=1):
        profit_rate = calculate_stock_data(stock)[3]
        print(f"{rank}位：{stock['name']} {profit_rate:+.2f}%")


# =========================
# 銘柄検索
# =========================

def search_stock(stock_list):
    """銘柄名から保有銘柄を検索する"""

    search_name = input("検索したい銘柄名：").strip()

    found = False

    for stock in stock_list:
        if stock["name"] == search_name:
            purchase_total, current_value, profit, profit_rate = (
                calculate_stock_data(stock)
            )

            print("\n==== 検索結果 ====")
            print(f"銘柄：{stock['name']}")
            print(f"株数：{stock['shares']:,}株")
            print(f"購入価格：{stock['price']:,.1f}円")
            print(f"現在価格：{stock['current_price']:,.1f}円")
            print(f"評価損益：{profit:+,.1f}円")
            print(f"評価損益率：{profit_rate:+.2f}%")

            found = True

    if not found:
        print("銘柄が見つかりませんでした")


# =========================
# メイン処理
# =========================

def main():

    while True:
        print("\n==== 資産管理アプリ ====")
        print("1. 銘柄登録")
        print("2. 保有銘柄一覧")
        print("3. 評価損益ランキング")
        print("4. 銘柄検索")
        print("5. 現在評価額合計")
        print("6. 年間配当金合計")
        print("7. 終了")

        choice = input("操作を選択してください：")

        if choice == "1":
            register_stock(stocks)

        elif choice == "2":
            show_stocks(stocks)

        elif choice == "3":
            show_ranking(stocks)

        elif choice == "4":
            search_stock(stocks)

        elif choice == "5":
            total_value = calculate_total_current_value(stocks)
            print(f"現在評価額合計：{total_value:,.1f}円")

        elif choice == "6":
            total_dividend = calculate_total_dividend(stocks)
            print(f"年間配当金合計：{total_dividend:,.1f}円")

        elif choice == "7":
            print("アプリを終了します")
            break

        else:
            print("正しい番号を入力してください")


if __name__ == "__main__":
    main()
