import mysql.connector
import pandas as pd
import Project
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
def timet():
    print('--------------------------------------------')
    print()
    print('TO VIEW THE TIMINGS PRESS 1')
    print()
    print("TO GO BACK TO MAIN MENU PRESS 2")
    print()
    time=int(input("ENTER YOUR CHOICE: "))
    if time==1:
        print('--------------------------------------------')
        print()
        print("TO VIEW THE TIMING OF JABAL TRADERS PRESS 1 ")
        print()
        print("TO VIEW THE TIMING OF ALI REPAIRS PRESS 2 ")
        print()
        choice=int(input("ENTER YOUR CHOICE: "))
        if choice==1:
            print('--------------------------------------------')
            read=pd.read_sql("select OPENING_TIME from Jabal_Time",mydb)
            read1=pd.read_sql("select CLOSING_TIME from Jabal_Time",mydb)
            a=read.iat[0,0]
            b=read1.iat[0,0]
            c=read.iat[1,0]
            d=read1.iat[1,0]
            print()
            print("OPENING TIME(morning): ",a)
            print("CLOSING TIME(evening): ",b)
            print()
            print("OPENING TIME(night): ",c)
            print("CLOSING TIME(night): ",d)
            print()
            print('--------------------------------------------')
        elif choice==2:
            print('--------------------------------------------')
            read=pd.read_sql("select OPENING_TIME from Ali_Time",mydb)
            read1=pd.read_sql("select CLOSING_TIME from Ali_Time",mydb)
            a=read.iat[0,0]
            b=read1.iat[0,0]
            c=read.iat[1,0]
            d=read.iat[1,0]
            print()
            print("OPENING TIME(morning): ",a)
            print("CLOSING TIME(evening): ",b)
            print()
            print("OPENING TIME(night): ",c)
            print("CLOSING TIME(night): ",d)
            print()
            print('--------------------------------------------')   
    elif time==2:
        print()
        Project.main()

        
                   
               
               
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    