name = input("銘柄名を入力してください：")
shares = input("株数を入力してください：")
price = input("株価を入力してください：")

print("銘柄:", name)
print("株数:", shares)
print("株価:", price)

total = shares * price
print("購入金額:", total)