number =int (input("enter number"))
if number==0:
    print("number =0")
elif number>0:
    if number % 2==0:
        print("عدد مثبت و زوج است")
    else:
        print("عدد مثبت و فرد است")
elif number<0:
    if number % 2==0:
        print("عدد منفی و زوج است")
    else:
        print("عدد منفی و فرد است")
