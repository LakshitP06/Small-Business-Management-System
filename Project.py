import password
import PASSWORDa
import Timing
import Stocks
import Admin
import Rating
def main():
    print('--------------------------------------------')
    print('***WELCOME TO EMPLOYEE MANAGEMENT SYSTEM***')
    print('--------------------------------------------')
    print()
    print('WE PROVIDE YOU WITH THESE SERVICES:')
    print()
    print('1. EMPLOYEE LOGIN')
    print()
    print('2. OPENING AND CLOSING TIME')
    print()
    print('3. STOCKS')
    print()
    print('4. ADMIN LOGIN')
    print()
    print('5. RATE THE SERVICE')
    print()
    print('6. EXIT')
    print()
    Service=int(input('PLEASE PICK THE NUMBER ASSOCIATED WITH YOUR SERVICE: '))
    if Service==1:
        print()
        print('--------------------------------------------')
        print('         COMPANIES REGISTERED ARE:          ')
        print()
        print('1. JABAL TRADERS')
        print('2. ALI REPAIRS')
        print()
        company=int(input('PLEASE PICK YOUR COMPANY: '))
        if company==1:
            password.password()
        elif company==2:
            PASSWORDa.PASSWORD()    
    elif Service==2:
        Timing.timet()
    elif Service==3: 
        Stocks.stock()
    elif Service==4:
        Admin.admin()
    elif Service==5:
        Rating.rate()
    elif Service==6:    
        print()
        print("THANK YOU FOR USING OUR SMALL BUSINESS MANAGEMENT SYSTEM")
        print('--------------------------------------------')