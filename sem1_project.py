#General stores management software
m=0
products=["Milk","Cheese","Butter","Chocolate","Juice","Chips","Biscuits","Maggie","Coffee"]
counts=[0,0,0,0,0,0,0,0,0]
bills = []

def do_billling():
    t=0
    more=0
    while(more==0):
        print("Enter the following product codes for input")
        print("Milk(70rs) = 1")
        print("Cheese(150rs) = 2")
        print("Butter(60rs) = 3")
        print("Chocolate(20rs) = 4")
        print("Juice(30rs) = 5")
        print("Chips(10rs) = 6")
        print("Biscuits(10rs) = 7")
        print("Maggie(15rs) = 8")
        print("Coffee(50rs) = 9")
        
        b=int(input("Enter Product"))
        if(b in range(1,10)):
            if(b==1):
                t=t+70
            elif(b==2):
                t=t+150
            elif(b==3):
                t=t+60
            elif(b==4):
                t=t+20
            elif(b==5):
                t=t+30
            elif(b==6):
                t=t+10
            elif(b==7):
                t=t+10
            elif(b==8):
                t=t+15
            elif(b==9):
                t=t+50
            counts[b-1]=counts[b-1]+1
            print("Total amout = ",t)
            print("Enter 0 to add more product")
            print("Enter 1 to checkout")
            more=int(input("Enter"))
            if(more==0):
                continue
        else:
            print("Enter Valid Number")
            continue
        return(t)

def show_history():
    for i in range(len(products)):
        print(products[i]," = ",counts[i])
    print(bills)

while(m!=2):
    print("Welcome to the Menu")
    print("Enter 0 to start billing")
    print("Enter 1 to check history")
    print("Enter 2 to exit")
    m=int(input("Enter "))
    if(m==0):
        total = do_billling()
        bills.append(total)
        print("Final total is", total)
    elif(m==1):
        show_history()
    elif(m==2):
        print("Thankyou")
    else:
        print("Enter valid operation")