enter_amount = input("How much do you have ?")
amount = int(enter_amount)
if amount <= 10:
    print(" you cannot go to the market")
else:    
    
    if amount <=20:
        print("we can buy yam")
    elif amount <= 30:
        print("we can buy yam and Egg")
    elif amount > 30:
        print ("we can buy more than yam and egg")
    else:
        print(" you have enough money to buy all we need")
#else:
    #print(" you cannot go to the market")
