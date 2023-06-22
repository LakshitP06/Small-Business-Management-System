#start of the program
#modules are inputted
import numpy as np
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
print('***WELCOME TO EMPLOYEE MANAGEMENT SYSTEM***')
print()
print('We provide you with these services:')
print('i.   Admin Login')
print('ii.  Opening and closing time')
print('iii. Hours of Schedule')
print('iv.  Contact Information')
print('If you want to exit the program press n')
print()
Service=input(' Please pick your concerned service:')

if Service=='Admin Login':
    print()
    print('The companies available are:')
    print('1,Jabal Traders')
    print('2.Oriet Travels')
    print('3.Delhi Darbar')
    company=input('Please pick your company: ')
    if company=='Jabal Traders':
         while True:
             passwd=int(input("Input the 4 digit Password to continue: "))
             if passwd==6497:
                 print()
                 print("Access Granted")
                 print()            
                 print('Welcome to Jabal traders Database')
                 print()
                 print('What would you like to do?')
                 print("Press 1 if  you want to update the timing")
                 print("Press 2 if you want to update the money structure and view")
                 do=int(input("Please choose : "))
                 if do==1:
                     print('Now you can update the timing')
                     Name=input('Enter your name : ')
                     Arrival=input('Enter the time you arrived : ')
                     Leaving=input('Enter the time you left : ')
                     date=input("Enter the date : ")
                     a=str(Name)
                     b=str(Arrival) 
                     c=str(Leaving)
                     st='insert into Jabal_Traders(NAME,ARRIVAL_TIME,LEAVING_TIME,DATE) values("{}","{}","{}","{}")'.format(a,b,c,date)
                     mycursor.execute(st)
                     mydb.commit()
    
                     mycursor.execute('select * from Jabal_Traders')
                     tab=mycursor.fetchall()
                     for i in tab:
                         print(i)
                 elif do==2:
                     Price=float(input("Enter the profit made: "))
                     mycursor.execute("insert into Jabal_Traders_Total(PRICE) values({})".format(Price))
                     mydb.commit()
                     read=pd.read_sql("select * from Jabal_Traders_Total",mydb)
                     p=read.values
                     x=np.linspace(100,1000.200)
                     plt.hist(p,x)
                     plt.xlabel("Money")
                     plt.ylabel("Sequence of incoming profit")
                     plt.title("Graph Representing The Average")
                     plt.show()
                     print("The Graph Is Represented Above")
                 else:
                     break    
                 break
             else:
                 print()
                 print("hmm...i think you made a mistake please retry)
