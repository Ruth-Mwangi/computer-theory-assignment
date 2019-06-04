money=0.00
vending_machine={"Ice Cream":"IC"}
prices={"Ice Cream":"60.00"}

#Functions
#def set_money(amount):
 #   global money
  #  money += amount
    
def purchase(required):
    global money
    
    if money>= required:
        print("Item Vended")
        print()
    else:
        print("Not enough money.")
        print()

def check(amount):
    global money
    if (amount == 20 or amount == 40):
        money=money+amount
        print()
        purchase(60.00)
    else:
        print("------------------------------------------------------------")
        print("|-------Vending Machine only accepts 20's and 40's---------|")
        print("------------------------------------------------------------")
        print()
        
def transaction(user_input):
    global money
    
    if user_input == "IC":
        print()
    else:
        print("Invalid Input!")
        print()
        
def main():
    #item_list=[]
    switch = 1 
    while switch==1:
        print("Welcome to the Vending Machine, vending machine only accepts 20's and 40's and does not give change.")
        print()
        print("Here are your selection and price.")
        print()
        print(vending_machine,prices)
        print()
        user_switch=1
        while user_switch ==1:
            user_input= input("Please input your selection: ").upper()

            transaction(user_input)
            print()
            while money<60: 
                print ("You currently have "+str(money)+" put in.")
                print()
                amount = int(input ("Please input money: "))
                print()
                check(amount)
                
            choice=1
            while choice == 1:
                user_input=input ("Are you done? (y/n): ").lower()
                if user_input == "y":
                    user_switch=0
                    choice=0
                    switch=0
                elif user_input=="n":
                    user_switch=1
                    choice=0
                else:
                    print("invalid option!")
                    choice=1
            
            


main()
                
            
            
        