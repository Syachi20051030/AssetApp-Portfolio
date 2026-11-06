def calculate_total(price,shares):
    return price * shares

stocks = []

while True:
    name = input("銘柄名を選択してください：")
    shares = int(input("株数を入力してください："))
    price = float(input("取得価格を入力してください："))
    current_price = float(input("現在価格を入力してください："))
    dividend = float(input("配当金を入力してください："))

    stock = {
        "name":name,
        "shares":shares,
        "price":price,
        "current_price":current_price,
        "dividend":dividend
    }

    stocks.append(stock)

    answer = input("もう1銘柄登録しますか？(yes/no)：")

    if answer == "no":
        break

print()
print("---- 保有銘柄一覧 ----")

total_assets = 0
current_assets = 0
total_dividend = 0

for stock in stocks:
    purchase_total = calculate_total(
        stock["price"],
        stock["shares"]
    )

    current_value = calculate_total(
        stock["current_price"],
        stock["shares"]
    )

    annual_dividend = stock["dividend"] * stock["shares"]

    profit = current_value - purchase_total
    #辞書登録しておく
    stock["profit"] = profit    
    profit_rate = profit / purchase_total*100

    print("銘柄：",stock['name'])
    print(f"株数：{stock['shares']:,}")
    print(f"取得価格：{stock['price']:,.1f}円")
    print(f"現在価格：{stock['current_price']:,.1f}円")
    print(f"購入総額：{purchase_total:,}円")
    print(f"現在評価額：{current_value:,}円")
    print(f"評価損益：{profit:+,.0f}円")
    print(f"評価損益率：{profit_rate:+.2f}%")
    print()
    print(f"1株あたり配当金：{stock['dividend']:,.1f}円")
    print(f"年間配当金：{annual_dividend:,.1f}円")
    print(f"取得価格ベース年間配当利回り：{(annual_dividend/purchase_total)*100:+.2f}%")
    print()
    
    total_assets += purchase_total
    current_assets += current_value
    total_dividend += annual_dividend

total_profit = current_assets - total_assets
total_profit_rate = total_profit / total_assets * 100
#sorted関数でprofitの値を基準に降順でソートする
profit_ranking = sorted(
    stocks, 
    key=lambda stock: stock["profit"], 
    reverse=True
)

print("-------------------------")
print(f"投資総額：{total_assets:,.1f}円")
print(f"現在評価額：{current_assets:,.1f}円")
print(f"評価損益合計：{total_profit:+,.1f}円")
print(f"評価損益率合計：{total_profit_rate:+.2f}%")
print(f"年間配当金合計：{total_dividend:,.1f}円")
print(f"取得価格ベース年間配当利回り合計：{total_dividend/total_assets*100:+.2f}%")
#表示する
print()
print("---- 評価損益ランキング ----")

rank = 1

for stock in profit_ranking:
    print(f"{rank}位：{stock['name']}：{stock['profit']:+,.0f}円")
    rank += 1