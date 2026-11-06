def calculate_total(shares, price):
    return shares * price
#新しい関数
def calculate_stock_data(stock):
    purchase_total = calculate_total(stock["shares"], stock["price"])
    current_value = calculate_total(stock["shares"], stock["current_price"])

    profit = current_value - purchase_total
    profit_rate = profit / purchase_total * 100

    return purchase_total, current_value, profit, profit_rate

def show_stocks():
    print("保有銘柄一覧を表示します")
    print()
    print("----保有銘柄一覧----")

    total_assets = 0
    current_assets = 0
    total_dividend = 0

    for stock in stocks:
        purchase_total, current_value, profit, profit_rate = calculate_stock_data(stock)
        annual_dividend = stock["dividend"] * stock["shares"]

        print("銘柄：", stock["name"])
        print("株数：", stock["shares"])
        print(f"購入価格：{stock["price"]:,.1f}円")
        print(f"現在価格：{stock["current_price"]:,.1f}円")
        print(f"購入総額：{purchase_total:,.1f}円")
        print(f"現在評価額：{current_value:,.1f}円")
        print(f"評価損益：{profit:+,.1f}円")
        print(f"評価損益率：{profit_rate:+.2f}%")
        print()
        print(f"一株あたり配当金：{stock["dividend"]:,.1f}円")
        print(f"年間配当金：{annual_dividend:,.1f}円")
        print(f"取得価格ベース配当利回り：{stock["dividend"] / stock["price"] * 100:.2f}%")
        print()

        total_assets += purchase_total
        current_assets += current_value
        total_dividend += annual_dividend

    total_profit = current_assets - total_assets
    total_profit_rate = total_profit / total_assets * 100

    print("-------------------------")
    print(f"投資総額：{total_assets:,.1f}円")
    print(f"現在評価額：{current_assets:,.1f}円")
    print(f"評価損益合計：{total_profit:+,.1f}円")
    print(f"評価損益率合計：{total_profit_rate:+,.2f}%")
    print(f"年間配当金合計：{total_dividend:,.1f}円")
    print(f"取得価格ベース配当利回り合計：{total_dividend / total_assets * 100:,.2f}%")
    print()

#ランキングの処理
def show_ranking():
    print("評価損益ランキングを表示します")

    for stock in stocks:
        purchase_total, current_value, profit, profit_rate = calculate_stock_data(stock)
    
        stock["profit"] = profit
        stock["profit_rate"] = profit_rate
                
    profit_ranking = sorted(stocks, key=lambda stock:stock["profit"], reverse = True)
    profit_rate_ranking = sorted(stocks, key=lambda stock:stock["profit_rate"], reverse = True)
    
    print()
    print("----評価損益ランキング----")
    
    rank = 1
    for stock in profit_ranking:
        print(f"{rank}位：{stock['name']}:{stock['profit']:+,.0f}円")
        rank += 1
    
    print()
    print("----評価損益率ランキング----")
    
    rank = 1
    for stock in profit_rate_ranking:
        print(f"{rank}位：{stock['name']}:{stock['profit_rate']:+,.2f}%")
        rank += 1
    
    

#検索の処理
def search_stock():
    print("銘柄検索を行います")
    search_name = input("検索したい銘柄名：")
    
    found = False
    
    print()
    print("---- 検索結果 ----")
    
    for stock in stocks:
        if stock["name"] == search_name:
            purchase_total, current_value, profit, profit_rate = calculate_stock_data(stock)
    
            print("銘柄：", stock["name"])
            print(f"株数：{stock['shares']:,}株")
            print(f"購入価格：{stock['price']:,.1f}円")
            print(f"現在価格：{stock['current_price']:,.1f}円")
            print(f"評価損益：{profit:+,.0f}円")
            print(f"評価損益率：{profit_rate:+.2f}%")
    
            found = True
    
    if found == False:
            print("銘柄が見つかりませんでした")

stocks = []

while True:
    name = input("銘柄を入力してください：")
    shares = int(input("株数を入力してください："))
    price = float(input("購入価格を入力してください："))
    current_price = float(input("現在価格を入力してください："))
    dividend = float(input("配当金を入力してください："))

    stock = {
        "name" : name,
        "shares" : shares,
        "price" : price,
        "current_price" : current_price,
        "dividend" : dividend
    }

    stocks.append(stock)

    answer = input("追加で入力しますか？yes/no：")

    if answer == "no":
        break

while True:
    print()
    print("====資産管理アプリ====")
    print("1.保有銘柄一覧")
    print("2.評価損益ランキング")
    print("3.銘柄検索")
    print("4.終了")

    choice = input("操作を選択してください：")

    if choice == "1":
        show_stocks()

    elif choice == "2":
        show_ranking()

    elif choice == "3":
        search_stock()

    elif choice == "4":
        print("アプリを終了します")
        break

    else:
        print("正しい番号を入力してください")