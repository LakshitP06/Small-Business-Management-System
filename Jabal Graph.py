import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
import pandas as pd
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='program')
mycursor=mydb.cursor()
read=pd.read_sql("select * from Jabal_Traders_Total",mydb)
p=read.values
x=np.linspace(100,1000.200)
plt.hist(p,x,range=[100,200])
