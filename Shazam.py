import mysql.connector 
import pandas as pd
import matplotlib.pyplot as plt
mydb=mysql.connector.connect(host="localhost", user="root", passwd="123456789", database="program")
mycursor=mydb.cursor()
print('PLEASE RATE YOUR EXPERIENCE:')
print('1 BEING THE LOWEST AND 5 BEING THE HIGHEST')
def rate():
    rate=int(input('ENTER: '))
    mycursor.execute("insert into rating(rate) values({})".format(rate))
    mydb.commit()
    read=pd.read_sql("select * from rating",mydb)
    n=read.values
    a=1
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    for i in range(0,len(n)):
        y=read.iat[i,0]
        if y==1:
            list1.append(a)
            a1=len(list1)
        elif y==2:
            list2.append(a)
            b1=len(list2)
        elif y==3:
            list3.append(a)
            c1=len(list3)
        elif y==4:
            list4.append(a)
            d1=len(list4)
        elif y==5:
            list5.append(a)
            e1=len(list5)
    x=[1,2,3,4,5]
    final=[a1,b1,c1,d1,e1]
    plt.bar(x,final)
    plt.xticks(x)
    plt.xlabel("RATINGS")
    plt.ylabel("NUMBER OF PEOPLE")
    plt.title("RATING")
    
    
