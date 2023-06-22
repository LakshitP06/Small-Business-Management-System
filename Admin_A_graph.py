import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
import Admin_A
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
def graph():
    print('--------------------------------------------')
    print()
    print("TO VIEW THE CURRENT GRAPH PRESS 1")
    print()
    print("TO SAVE THE CURRENT GRAPH AND START A NEW ONE PRESS 2")
    print()
    option1=int(input("ENTER YOUR CHOICE: "))
    if option1==1:
        read=pd.read_sql("select * from Ali_Repairs_Total",mydb)
        p=read.values
        list1=[]
        list2=[]
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
        plt.show()
        print('--------------------------------------------')
        print("    THE GRAPH IS REPRESENTED ABOVE!         ")
        print('--------------------------------------------')      
    elif option1==2:
        print('--------------------------------------------')
        print()
        print("TO CONFIRM PRESS 1: ")
        print("(it deletes the graph for a new one)")
        print()
        print('TO RETURN TO THE ADMIN MENU PRESS 2')
        numb=int(input("ENTER YOUR CHOICE: "))
        if numb==1:
            month=str(input("ENTER THE MONTH: "))
            year=int(input("ENTER THE YEAR:: "))
            year1=str(year)
            read=pd.read_sql("select * from Ali_Repairs_Total",mydb)
            p=read.values
            list3=[]
            list4=[]
            for j in range(1,len(p)+1):
                list3.append(j)
            x=list3
            read1=pd.read_sql("select *from Ali_Repairs_Total",mydb,index_col='sno')
            for i in range(0,len(p)):
                a=read1.iat[i,0]
                list4.append(a)
            y=list4
            plt.plot(x,y,'k',marker='*',markeredgecolor='r',markerfacecolor='r')
            plt.xticks(x)
            plt.xlabel("DAYS")
            plt.ylabel("INCOME")
            plt.title("INCOME GRAPH")
            month1="C:\\users\\laksh\\ip project\\Graphs_For_Ali_Repairs\\"+"Income"+' '+month+' '+year1+'.pdf'
            plt.savefig(month1)
            mycursor.execute("Truncate table Ali_Repairs_Total")
            mydb.commit()
            plt.stop()
            print()
            print('--------------------------------------------')
            print("        YOU CAN RESTART THE SYSTEM!         ")
            print('--------------------------------------------')     
        elif numb==2:
            Admin_A.admina()
          
        