myorders = []
sum =0
#details of ferm
print("Welcome to our store")
print("Chitkara Fashion Arena")
print("Rajpura,Punjab")
print("GSTIN:22AAAAA0000A1Z5") 
print("")
print("")

        # dictionary to be created
def shop(sum):
     dict={'jeans':5000,'hoodies':1000,'tie':400,'trouser':900,'tuxedo':10000,'bow':300,'blazer':6000,'windcheater':3000}
     print(list(dict.keys()))
     True

#       inventory
     while True:
         print("jeans(5000rs)")
         print("hoodies(1000)")
         print("tie(400)")
         print("trouser(900)")
         print("tuxedo(10000)")
         print("bow(300)")
         print("blazer(6000)")
         print("windcheater(3000)")
         order = input("type what you wanna buy: ")
         if order =="E":
            break

#          quantity
#          discount
         else:
             if order in dict.keys():
                 quantity = int(input("How much do you want: "))
                #  d=int(input("discount given :"))
                 oneItem = f"order: {order}, quantity: {quantity} "
                 myorders.append(oneItem)
                 sum=sum+quantity*(dict[order])
                #  sum=sum-(sum*(d/100))
#                  sum=sum+quantity*(dict[order])-(discount/100)*100

             else:
                 print("please enter right item.⚠️ ")
     return sum
        
sum = shop(sum)
print(myorders)
print("your total bill is ",sum)
print("Do you wanna add more item. press: yes otherwise no")
opinion = input()

if opinion=="yes":
   sum = shop(sum)
   print(myorders)

#          mode of payment 
else:
    print("ThankYou for coming to our shop. Please handover money.")
mess=input("press 1 for cash and 2 for card :")
bill=sum

#          cash
if mess=='1':
    sum=sum-(sum*(1/10))
    print("your total bill is ",sum)
    cash=int(input("your given amount :"))   
    left_cash=cash-sum
    print("cash to be return :",left_cash)
    print("")
    print(myorders)
    print("your total bill is ",sum)
    print("")
    print("")
    print("visit again 🙏")

#          card
elif mess=='2':
    bill=sum-(sum*(1/10))
    print('Your total bill is',bill)
    exit()