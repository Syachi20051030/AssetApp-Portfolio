def calculate_total(price,shares):
    return price * shares

stocks = []

while True:
    name = input("銘柄名を選択してください：")
    shares = int(input("株数を入力してください："))
    price = int(input("価格を入力してください："))

    stock = {
        "name":name,
        "shares":shares,
        "price":price
    }

    stocks.append(stock)

    answer = input("もう1銘柄登録しますか？(yes/no)：")

    if answer == "no":
        break

print()
print("---- 保有銘柄一覧 ----")

total_assets = 0

for stock in stocks:
    total = calculate_total(
        stock["price"],
        stock["shares"]
    )

    print("銘柄：",stock["name"])
    print("株数：",stock["shares"])
    print("取得価格：",stock["price"])
    print("購入総額：",total)
    print()
    
    #total_assets += totalでも可
    total_assets = total_assets + total

print("-------------------------")
print("投資総額：", total_assets)