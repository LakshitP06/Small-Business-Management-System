import Alit
import Alig
import Project
def PASSWORD():
    while True:
        passwd=int(input("INPUT YOUR 4 DIGIT PASSWORD: "))
        if passwd==2750:
            print("ACCESS GRANTED")
            print()    
            print('--------------------------------------------')    
            print('      WELCOME TO ALI REPAIRS DATABASE        ')
            print('--------------------------------------------') 
            print()
            print('WHAT WOULD YOU LIKE TO DO:')
            print()
            print("PRESS 1 TO UPDATE THE TIMING")
            print()
            print("PRESS 2 TO UPDATE THE INCOME")
            print()
            print("PRESS 3 TO EXIT TO MAIN MENU")
            print()
            do=int(input("ENTER YOUR CHOICE: "))
            print('--------------------------------------------')
            if do==1:
                Alit.Alit()
            elif do==2:
                Alig.Alig()
            elif do==3:
                print()
                Project.main()
            break
        else:
            print()
            print("HMM...I THINK YOU MADE A MISTAKE PLEASE RETRY")
           