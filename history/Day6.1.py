#関数を作る
def hello():
    print("こんにちは")

hello()

def greet(name):
    print("こんにちは", name)

greet("Yuya")

def calculate_total(price, shares):
    return price * shares

total = calculate_total(3608, 45)

print(total)


def calculate_total(price, shares):
    return price * shares

stock1 = {
    "name" : "INPEX",
    "shares" : 45,
    "price" : 3608
}

total = calculate_total(
    stock1["price"],
    stock1["shares"]
)

print("銘柄：", stock1["name"])
print("購入総額：", total)