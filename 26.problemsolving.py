def cal_h():

    massege = '''
    -------------------------------------
          walcome to calculator
    -------------------------------------
     
     1. addition
     2. subtraction
     3. multipilaction
     4. exit

     ------------------------------------
     note: remeber only enter number
     enter 1 or 2 or 3 for any of calculation:
     '''

    option = int(input(massege))


    if option == 1:
        addition()    
    elif  option ==2:
        subtraction() 
    elif option ==3:
        multipilaction()
    elif option == 4:
        exit()
    else:
        print('\n you enter worng choice. try again')

def addition():
    try:
        a = int(input(' enter 1st number:'))
        b = int(input('enter 2nd numbber:'))
    except:
        print('\nOnly allow interger numebrs.')
        cal_h()
    else:
        sum =  a + b
        print('\n addition answer:', sum)
        cal_h()

def subtraction():

    a = int(input('enter 1st number'))
    b = int(input('enter 2nd number'))
    sum = a * b
    print('\n subtraction answer:', sum)
    cal_h()
    

def multipilaction():
    a = int(input(' enter 1st number:'))
    b = int(input('enter 2nd numbber:'))
    sum =  a * b
    print('\n addition answer:', sum)
    cal_h()


massege = '''
-------------------------------------
        walcome to calculator
-------------------------------------
    
    1. addition
    2. subtraction
    3. multipilaction
    4. exit

    ------------------------------------
    note: remeber only enter number
    enter 1 or 2 or 3 for any of calculation:
    '''

option = int(input(massege))

if option == 1:
    addition()    
elif  option ==2:
    subtraction() 
elif option ==3:
    multipilaction()
elif option == 4:
    exit()
else:
    print('\n you enter worng choice. try again')