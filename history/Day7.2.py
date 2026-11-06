name = input("銘柄名を入力してください：")
#文字を数字に変えるstr→int
shares = int(input("株数を入力してください："))
price = int(input("株価を入力してください："))

print("銘柄：", name)
print("株数：", shares)
print("株価：", price)

total = shares * price
print("購入金額：", total)