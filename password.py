import Project
import jabalt
import jabalg
def password():
    while True:
        passwd=int(input("INPUT YOUR 4 DIGIT PASSWORD: "))
        if passwd==6497:
            print("ACCESS GRANTED")
            print()
            print('--------------------------------------------')         
            print('         WELCOME TO JABAL TRADERS           ')
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
            print()
            print('--------------------------------------------')
            if do==1:
                jabalt.jabalt()
            elif do==2:
                jabalg.jabalg()
            elif do==3:
                print()
                Project.main()
            break
        else:
            print()
            print("HMM...I THINK YOU MADE A MISTAKE PLEASE RETRY")

            