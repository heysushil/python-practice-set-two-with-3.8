'''
Error Handling concept:

Error handling me 4 block of area use kiya jata hai:

1. try: code ko yaha par check kiya jata hai
2. except: code agar sahi hai then yaha par aayega
3. finally: at last sub close karne ke liye
4. else: last message show karane ke liye

Raise keywork ka use:
1. raise keywork ka use single line error handle ke liye kiya jata hai.

Multiple errors:

1. syntax error
2. type error
3. intentation error
4. ModuleNotFoundError
5. Name error
'''

# try this code at first if it's occure problem then trnserfter to except

try:
    name = '100'
    print('\nName: ', int(name))
# for name error
except NameError:
    print('\nName variable define to karo?')
except ValueError:
    print('\nKewal integer number allowed hain?')
except:
    print('\nKoi aur porblem hain.')
else:
    print('\nNumber is ', name)
finally:
    print('\nAt last we close aur work.')


# example
try:
    option = int(input('\nEnter your option: '))
except ValueError:
    print('\nTry with 1 or integer numbers only.')
else:
    if option == 1:
        print('\nWelcome to option 1.')
    elif option == 2:
        print('\nExit.')
    else:
        print('\nWelcome to no options.')

