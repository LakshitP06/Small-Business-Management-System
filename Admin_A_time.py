import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
def timea():
    print('--------------------------------------------')
    print()
    print('TO VIEW THE CURRENT TABLE PRESS 1')
    print()
    print('TO SAVE THE TABLE AND START A NEW ONE PRESS 2')
    ok=int(input('ENTER YOUR CHOICE: '))
    if ok==1:
        mycursor.execute("select * from Ali_Repairs")
        tab=mycursor.fetchall()
        df=pd.DataFrame(tab, columns=mycursor.column_names)
        print()
        print(df)
        print()    
        print("THE TABLE IS REPRESENTED ABOVE")   
        print('--------------------------------------------')
    elif ok==2:
        print('--------------------------------------------')
        print()
        month=input('ENTER THE MONTH: ')
        year=input('ENTER THE YEAR: ')
        mycursor.execute("select * from Ali_Repairs")
        tab=mycursor.fetchall()
        df=pd.DataFrame(tab, columns=mycursor.column_names)
        a="C:\\users\\laksh\\ip project\\Timing_For_Ali_Repairs\\"+"Time"+' '+month+' '+year+'.csv'    
        df.to_csv(a)
        mycursor.execute("truncate table Ali_Repairs")
        mydb.commit()
        print('THE TABLE HAS BEEN SAVED')
        print('--------------------------------------------')
        