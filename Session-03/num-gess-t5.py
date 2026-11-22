import random
number  =random.randint(1,100)
print("number between 1 and 100")
for i in range (7):
    guess=int(input("enter your guess: "))

    if guess == number:
        print("winner")
        break
    elif guess> number:
        print("your number is too big")
    else :
         print("your number is too small")

else:
    print ("lost")
    print("the correct number was:",number)