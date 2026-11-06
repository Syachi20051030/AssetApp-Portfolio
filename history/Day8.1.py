stocks = []

name = input("銘柄名を入力してください：")
shares = int(input("株数を入力してください："))
price = int(input("株価を入力してください："))

stock = {
    "name": name,
    "shares": shares,
    "price": price
}

stocks.append(stock)
