def calculate_total(price,shares):
    return price * shares

stocks = []

while True:
    name = input("銘柄名を選択してください：")
    shares = int(input("株数を入力してください："))
    price = float(input("取得価格を入力してください："))
    current_price = float(input("現在価格を入力してください："))

    stock = {
        "name":name,
        "shares":shares,
        "price":price,
        "current_price":current_price
    }

    stocks.append(stock)

    answer = input("もう1銘柄登録しますか？(yes/no)：")

    if answer == "no":
        break

print()
print("---- 保有銘柄一覧 ----")

total_assets = 0
current_assets = 0

for stock in stocks:
    purchase_total = calculate_total(
        stock["price"],
        stock["shares"]
    )

    current_value = calculate_total(
        stock["current_price"],
        stock["shares"]
    )

    profit = current_value - purchase_total
    #評価損益率計算式
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
    
    total_assets += purchase_total
    current_assets += current_value

#全銘柄集計後に計算
#評価損益合計 = 現在評価額 - 投資総額
total_profit = current_assets - total_assets
#評価損益率合計 = 評価損益合計 / 投資総額 * 100
total_profit_rate = total_profit / total_assets * 100

print("-------------------------")
print(f"投資総額：{total_assets:,.1f}円")
print(f"現在評価額：{current_assets:,.1f}円")
print(f"評価損益合計：{total_profit:+,.1f}円")
print(f"評価損益率合計：{total_profit_rate:+.2f}%")