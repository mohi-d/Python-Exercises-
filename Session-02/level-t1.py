Slevel =input("enter level: ")
price=float(input("enter price: "))

if level== "Gold":
    discount=20
elif level=="Silver":
    discount =10
else:
    discount=5

    if price >1000000:
        discount += 5

final_price=price -(price * discount/100)

print(discount)
print(final_price)

