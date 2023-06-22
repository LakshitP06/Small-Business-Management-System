import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
import matplotlib.pyplot as plt
import pandas as pd
import Project
def Alig():
    list1=[]
    list2=[]
    print("    NOW YOU CAN UPDATE THE PROFIT GRAPH       ")
    print()
    print("TO ENTER DATA PRESS 1")
    print()
    print('TO GO BACK TO THE MAIN MENU PRESS 2')
    print()
    val=int(input("ENTER YOUR CHOICE: "))
    if val==1:
        print('--------------------------------------------')
        Price=float(input("ENTER THE PROFIT FOR THE DAY: "))
        DATE=int(input("ENTER TODAY'S DATE(only the day number): "))
        print()
        print('--------------------------------------------')
        mycursor.execute("insert into Ali_Repairs_Total(PRICE,sno) values({},{})".format(Price,DATE))
        mydb.commit()
        read=pd.read_sql("select * from Ali_Repairs_Total",mydb)
        p=read.values
        for j in range(1,len(p)+1):
            list2.append(j)
        x=list2
        read1=pd.read_sql("select * from Ali_Repairs_Total",mydb,index_col='sno')
        for i in range(0,len(p)):
            a=read1.iat[i,0]
            list1.append(a)
        y=list1
        plt.plot(x,y,'k',marker='*',markeredgecolor='r',markerfacecolor='r')
        plt.xticks(x)
        plt.xlabel("DAYS")
        plt.ylabel("INCOME")
        plt.title("INCOME GRAPH")
        plt.close()
        print("YOUR INPUT IS RECORDED")
        print('--------------------------------------------')     
    elif val==2:
        print()
        Project.main()

  
            
    
        
    

