import Admin_A_time
import Admin_A_graph
import Admin_A_shoptime
import Admin_A_stocks
def admina():
    while True:
       passwd=int(input("ENTER YOUR 7 DIGIT PASSWORD: "))
       if passwd==8933616:
           print("ACCESS GRANTED")
           print()
           print('--------------------------------------------')         
           print('           WELCOME TO ALI REPAIRS           ')
           print('--------------------------------------------')
           print()
           print('TO VIEW THE TIMING TABLE PRESS 1')
           print()
           print('TO EDIT THE INCOME GRAPH PRESS 2')
           print()
           print('TO UPDATE THE SHOP TIMING PRESS 3')
           print()
           print('TO VIEW THE STOCKS PRESS 4')
           print()
           number1=int(input('ENTER YOUR CHOICE: '))
           if number1==1:
               Admin_A_time.timea()
           elif number1==2:
               Admin_A_graph.graph()
           elif number1==3:
               Admin_A_shoptime.shop()
           elif number1==4:
               Admin_A_stocks.stocks()
           break
       else:
           print()
           print("HMM...I THINK YOU MADE A MISTAKE PLEASE RETRY")      