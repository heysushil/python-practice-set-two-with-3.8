# stirng file 

name = 'Nikhil'
print('\nYour name is', name, '. Welcome to Python.')

# use concatation '+' in stirng
info = 'Hi, ' + name
# print(info)
welcomeMessage = 'Welcome to Python Language.'
endMessage = 'Thanks for studing.'

# show welcome message
print(info + '\n' + welcomeMessage + '\n' + endMessage)

# double qoute stirng of single line
name = "\nNikhil"
print(name)

# multiline string ke liye tripal single (''') ya double (""") qoute ka use kar sakte hain.
data = '''
---------------------------------------------------
                    Data
---------------------------------------------------
Your data
Your data
Your data                    
---------------------------------------------------
'''

data = """
---------------------------------------------------
                    Data
---------------------------------------------------
Your data
Your data
Your data                    
---------------------------------------------------
"""
print(data)


# use stirng as index
name = 'Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python Welcome to Hello Python'
print('\nName: ', name, ' name[0]: ', name[0], ' name[3]: ', name[3])

# Slicing me range jo hai wo (n-1) tak chalta hai.
print('\nOnly get 1st word: ', name[0:7])
print('\nOnly provide start number: ', name[11:])
print('\nOnly provide last number: ', name[:11])

# negative range
print('\nGet last char: ', name[-1])
print('\nGet last word: ', name[-6:])

# chekc length of stirng
print('\nCheck length of name: ', len(name))

# string methos
name = 'Hello Nikhil'
print('\nCheck N: ', name.index('N'))
print('\nCapatilze: ', name.capitalize())
print('\nUpper case: ', name.upper())
print('\nLower case: ', name.lower())

newdata = name.split(' ')
print('\nNew data: ', newdata)

'''
Programs:

1. Multiline string ka use karke apna bio data banana hai.
2. Apne friends name ke variable banae hai aur unko print karna hai ek sath.
3. Friend variables ka use karke har ek friend ke bar me thoda ka info dena hai print ka use karke.
Like as:
    yourFriend variable data: about your friend
'''