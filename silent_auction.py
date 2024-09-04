import os
from silent_aution_art import logo
print(logo)
def aution(countinue_auction , list_of_auction):
    while countinue_auction=="yes":
      user_name=input("what is your name: ")
      money=int(input("how much money you want to bid: "))
      list_of_auction[user_name]=money
      countinue_auction=input("is there any more people left to bid: ")
      os.system("cls")
    k=0
    d=''
    for i in list_of_auction:
       if list_of_auction[i]>int(k):
          k=list_of_auction[i]
          d=i
    print(d,k)

list_of_auction={}
countinue_auction= "yes"   
aution(countinue_auction, list_of_auction)
