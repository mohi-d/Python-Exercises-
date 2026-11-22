import random
lenght=int(input("enter password lenght: "))
characters="abcdefghijklmnopqrstuvwxyzABCDELGDRGR"LRFHFRLLFDLTUVWXYZ0123456789"
password=""


for i in range(lenght):
    password +=random.choice(charecters)
    
    print("your password is:",password)