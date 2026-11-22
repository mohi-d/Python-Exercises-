year =int(input("enter year: "))

if year % 100 == 0 and  year % 400 ==0:
    print ("کبیسه است")

elif year %4==0:
      print("کبیسه است")

else :
    print("کبیسه نیست")
