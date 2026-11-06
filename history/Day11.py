def calculate_total(price,shares):
    return price * shares

stocks = []

while True:
    name = input("銘柄名を選択してください：")
    shares = int(input("株数を入力してください："))
    #小数点以下まで変換する場合はfloat使用する
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

    print("銘柄：",stock["name"])
    #カンマ表示したい場合はprint(f"{1000:,}"),小数点以下を表示する場合は.1fを加える
    print(f"株数：{stock["shares"]:,}")
    print(f"取得価格：{stock["price"]:,.1f}円")
    print(f"現在価格：{stock["current_price"]:,.1f}円")
    print(f"購入総額：{purchase_total:,}円")
    print(f"現在評価額：{current_value:,}円")
    print(f"評価損益：{profit:+,.0f}円")
    print()
    
    total_assets += purchase_total
    current_assets += current_value

print("-------------------------")
print(f"投資総額：{total_assets:,.1f}円")
print(f"現在評価額：{current_assets:,.1f}円")
print(f"評価損益合計：{current_assets - total_assets:+,.1f}円")