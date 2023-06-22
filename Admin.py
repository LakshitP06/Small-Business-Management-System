import Admin_J
import Admin_A
import Project
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
import pandas as pd
def admin():
    print()
    print('--------------------------------------------')
    print('       WELCOME TO ADMINISTRATION PAGE       ')
    print()
    print("TO ACCESS JABAL TRADERS DATABASE PRESS 1")
    print()
    print('TO ACCESS ALI REPAIRS DATABASE PRESS 2')
    print()
    print('TO VIEW CUSTOMER REVIEWS PRESS 3')
    print()
    print('TO GO BACK TO THE MAIN MENU PRESS 4')
    number=int(input('ENTER YOUR CHOICE: '))
    print('--------------------------------------------')   
    if number==1:
        Admin_J.adminj()
    elif number==2:
        Admin_A.admina()
    elif number==3:
        print()
        a=pd.read_sql('select * from rate',mydb)
        n=a.values
        pd.options.display.max_colwidth
        print(n)
    elif number==4:
        Project.main()
