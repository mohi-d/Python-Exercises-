mojodi =1000000

while True:
    print("1. check mojodi")
    print("2. variz money")
    print("3. bardasht money")
    print("4. exit")
    choice =input("choice an option: ")    

    if choice =="1":
       print("your mojodi is: " ,mojodi,"toman")
    elif choice =="2":
      amount=int(input("enter variz amount: "))
      if amount <=mojodi :
         mojodi = mojodi - amount
         print("variz successful")
         print ("your new mojodi is: ", mojodi)
      else:
         print("eror mojodi")

    elif choice == "3":
        amount = int(input("Enter bardasht amount: "))

        mojodi = mojodi + amount

        print("bardasht successful!")
        print("Your new mojodi is:", mojodi)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
          

