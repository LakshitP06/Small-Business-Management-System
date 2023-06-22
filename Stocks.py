import mysql.connector
import Project
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
def stock():
    print('--------------------------------------------') 
    print()
    print("TO INPUT THE STOCKS OF JABAL TRADERS PRESS 1")
    print()
    print('TO INPUT THE STOCKS OF ALI REPAIRS PRESS 2')
    print()
    print("TO GO BACK TO THE MAIN MENU PRESS 3")
    print()
    numb=int(input("ENTER YOUR CHOICE: "))
    Query='y'
    if numb==1:
        print('--------------------------------------------')
        while True:
            passwd=int(input("INPUT YOUR 4 DIGIT PASSWORD: "))
            if passwd==6497:
                print("ACCESS GRANTED")
                print()
                print("TO INPUT THE NEW STOCKS PRESS 1")
                print()
                print("TO INPUT THE STOCKS SOLD PRESS 2")
                print()
                print("TO GO BACK TO THE MAINE MENU PRESS 3")
                
                var=int(input("ENTER YOUR CHOICE: "))
                if var==1:
                    print('--------------------------------------------')
                    while Query=='y':
                        sno=int(input("ENTER THE SERIAL NUMBER: "))
                        prod=int(input("ENTER THE PRODUCTID: "))
                        name=input("ENTER THE NAME OF THE PRODUCT: ")
                        quantity=int(input("ENTER THE QUANTITY OF THE PRODUCT: "))
                        date=input("ENTER THE DATE: ")
                        price=float(input("ENTER THE PRICE OF ONE ITEM: "))
                        mycursor.execute("insert into Jabal_Traders_Stocks values({},{},'{}',{},{},{},'{}')".format(sno,prod,name,quantity,price,(quantity*price),date))
                        mydb.commit()
                        print()
                        Query=input("TO KEEP ENTERING PRODUCTS PRESS y:")
                        if Query!='y':
                            break
                    print()        
                    print("THANK YOU FOR THE INPUT")  
                    print('--------------------------------------------')
                    break
                elif var==2:
                    print('--------------------------------------------')
                    while Query=='y':
                        sno=int(input("ENTER THE SERIAL NUMBER: "))
                        prod=int(input("ENTER THE PRODUCTID: "))
                        name=input("ENTER THE NAME OF THE PRODUCT: ")
                        quantity=int(input("ENTER THE QUANTITY OF THE PRODUCT: "))
                        date=input("ENTER THE DATE: ")
                        price=float(input("ENTER THE PRICE OF ONE ITEM: "))
                        mycursor.execute("insert into Jabal_Traders_Stocks_sold values({},{},'{}',{},{},{},'{}')".format(sno,prod,name,quantity,price,(quantity*price),date))
                        mydb.commit()
                        print()
                        Query=input("TO KEEP ENTERING PRODUCTS PRESS y:")
                        if Query!='y':
                            break
                    print()        
                    print("THANK YOU FOR THE INPUT")  
                    print('--------------------------------------------') 
                    break
                elif var==3:
                    print()
                    Project.main()
            else:
                print()
                print("HMM...I THINK YOU MADE A MISTAKE PLEASE RETRY")
    elif numb==2:
        print('--------------------------------------------')
        while True:
            passwd=int(input("INPUT YOUR 4 DIGIT PASSWORD: "))
            if passwd==2750:
                print("ACCESS GRANTED")
                print()
                print("TO INPUT THE NEW STOCKS PRESS 1")
                print()
                print("TO INPUT THE STOCKS SOLD PRESS 2")
                print()
                print("TO GO BACK TO THE MAINE MENU PRESS 3")
                print()
                var=int(input("ENTER YOUR CHOICE: "))
                if var==1:
                    while Query=='y':
                        sno=int(input("ENTER THE SERIAL NUMBER: "))
                        prod=int(input("ENTER THE PRODUCTID: "))
                        name=input("ENTER THE NAME OF THE PRODUCT: ")
                        quantity=int(input("ENTER THE QUANTITY OF THE PRODUCT: "))
                        date=input("ENTER THE DATE: ")
                        price=float(input("ENTER THE PRICE OF ONE ITEM: "))
                        mycursor.execute("insert into Ali_Repairs_Stocks values({},{},'{}',{},{},{},'{}')".format(sno,prod,name,quantity,price,(quantity*price),date))
                        mydb.commit()
                        print()
                        Query=input("TO KEEP ENTERING PRODUCTS PRESS y:")
                        if Query!='y':
                            break
                    print()    
                    print("THANK YOU FOR THE INPUT")  
                    print('--------------------------------------------')    
                elif var==2:
                    while Query=='y':
                        sno=int(input("ENTER THE SERIAL NUMBER: "))
                        prod=int(input("ENTER THE PRODUCTID: "))
                        name=input("ENTER THE NAME OF THE PRODUCT: ")
                        quantity=int(input("ENTER THE QUANTITY OF THE PRODUCT: "))
                        date=input("ENTER THE DATE: ")
                        price=float(input("ENTER THE PRICE OF ONE ITEM: "))
                        mycursor.execute("insert into  Ali_Repairs_Stocks_sold values({},{},'{}',{},{},{},'{}')".format(sno,prod,name,quantity,price,(quantity*price),date))
                        mydb.commit()
                        print()
                        Query=input("TO KEEP ENTERING PRODUCTS PRESS y:")
                        if Query!='y':
                            break     
                    print()        
                    print("THANK YOU FOR THE INPUT")  
                    print('--------------------------------------------')
                    break
                elif var==3:
                    print()
                    Project.main() 
            else:
                print()
                print("HMM...I THINK YOU MADE A MISTAKE PLEASE RETRY")
    elif numb==3:
        print()
        Project.main()

                
                
                        
                        
                    
                        
                          
                        
                        
                
        
            
        
