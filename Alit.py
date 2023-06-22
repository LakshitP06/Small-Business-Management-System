import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
import Project
def Alit():
    print('      NOW YOU CAN UPDATE THE TIMING         ')
    print()
    print("TO INPUT DATA PRESS 1")
    print()
    print("TO GO BACK TO MAIN MENU PRESS 2")
    print()
    choice=int(input('ENTER YOUR CHOICE: '))
    print('--------------------------------------------')
    if choice==1:
        Name=input('ENTER YOUR NAME: ')
        Arrival=input('ENTER THE TIME YOU ARRIVED: ')
        Leaving=input('ENTER THE TIME YOU LEFT: ')
        date=input("ENTER THE DATE: ")
        print()
        print('--------------------------------------------')
        a=str(Name)
        b=str(Arrival) 
        c=str(Leaving)
        st='insert into Ali_Repairs(NAME,ARRIVAL_TIME,LEAVING_TIME,DATE) values("{}","{}","{}","{}")'.format(a,b,c,date)
        mycursor.execute(st)
        mydb.commit()
        print("YOUR INPUT IS REGISTERED")
        print('--------------------------------------------')
    elif choice==2:
        print()
        Project.main()

        
        
        
        
       

        
        
        
        
        
        
        
        
        
        
        
        
        
    