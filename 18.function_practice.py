# again choice
def again_choice():
    # user se option ke liye condtion
    message = '''
    ---------------------------------
        Welcome to Calculater
    ---------------------------------
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Exit
    ---------------------------------
    Note: Remeber only enter numbers.
    Enter 1 or 2 or 3 for any of calulation:    
    '''
    option = int(input(message))

    # check choice if 1 then show hello
    if option == 1:
        # print('\nHello')
        addition()
    # check choice if 2 then show hi
    elif option == 2:
        print('\nHi')
    # check if choice is wrong then show wrong
    elif option == 3:
        print('\n3')
    elif option == 4:
        print('\nExit')
    else:
        print('\nYou enter wrong choice. Try again')

# addition function
def addition():
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    sum = a + b
    print('\nAddition answer: ', sum)
    # dubara choice show karane ke liye again choice function banaya hai.
    again_choice()

# user se option ke liye condtion
message = '''
---------------------------------
    Welcome to Calculater
---------------------------------
1. Addition
2. Subtraction
3. Multiplication
4. Exit
---------------------------------
Note: Remeber only enter numbers.
Enter 1 or 2 or 3 or 4 for any of calulation:    
'''
option = int(input(message))

# check choice if 1 then show hello
if option == 1:
    # print('\nHello')
    addition()
# check choice if 2 then show hi
elif option == 2:
    print('\nHi')
# check if choice is wrong then show wrong
elif option == 3:
    print('\n3')
elif option == 4:
    print('\nExit')
# check if choice is wrong then show wrong
else:
    print('\nYou enter wrong choice. Try again')


