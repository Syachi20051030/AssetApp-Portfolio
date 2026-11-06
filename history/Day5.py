#辞書登録
stock1 = {
    "name" : "INPEX",
    "shares" : 45,
    "price" : 3608,
}

stock2 = {
    "name" : "野村不動産HD",
    "shares" : 150,
    "price" : 914,
}

stock3 = {
    "name" : "サイバーエージェント",
    "shares" : 85,
    "price" : 1308,
}

stock4 = {
    "name" : "日本製鉄",
    "shares" : 200,
    "price" : 640,
}

stock5= {
    "name" : "協立電機",
    "shares" : 80,
    "price" : 2354,
}

stock6 = {
    "name" : "三菱UFJ",
    "shares" : 100,
    "price" : 2585,
}

stocks = [stock1,stock2, stock3, stock4, stock5, stock6]

print(stock1["shares"])
print(stock1["name"])
print(stock1["price"])

total = stock1["shares"] * stock1["price"]

print("銘柄:", stock1["name"])
print("株数:", stock1["shares"])
print("取得価格:", stock1["price"])
print("購入金額:", total)

for stock in stocks:
    print("銘柄：", stock["name"])
    print("株数：", stock["shares"])
    print("取得価格：", stock["price"])