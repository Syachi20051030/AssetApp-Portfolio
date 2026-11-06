def calculate_total(price, shares):
    return price * shares

#辞書登録
stock1 = {
    "name" : "INPEX",
    "shares" : 45,
    "price" : 3608
}

stock2 = {
    "name" : "野村不動産HD",
    "shares" : 150,
    "price" : 914
}

stock3 = {
    "name" : "サイバーエージェント",
    "shares" : 85,
    "price" : 1308
}

stock4 = {
    "name" : "日本製鉄",
    "shares" : 200,
    "price" : 640
}

stock5= {
    "name" : "協立電機",
    "shares" : 80,
    "price" : 2354
}

stock6 = {
    "name" : "三菱UFJ",
    "shares" : 100,
    "price" : 2585
}

stocks = [stock1,stock2, stock3, stock4, stock5, stock6]

for stock in stocks:
    total = calculate_total(
        stock["price"],
        stock["shares"]
    )
    
    print("銘柄：", stock["name"])
    print("株数：", stock["shares"])
    print("取得価格：", stock["price"])
    print("購入総額:",total)
    print()

