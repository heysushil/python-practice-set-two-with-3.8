'''
Condition statments and practicale

Sytanx:

1. Jab single condition hoto:
    if your_condtion:
        your message. ye string ho ya kuch bhi ho sakta hai.

2. Jab single condition ho and ek default condtion ho to:
    if(your_condtion):
        your message. ye string ho ya kuch bhi ho sakta hai.
    else:
        your default message will be here.

3. Jab 1 se jada condition ho to:
    if(your_condtion):
        your message. ye string ho ya kuch bhi ho sakta hai.
    elif(your_another_condition):
        your message.
    else:
        default condition message.

4. Nested condition:
    if (your_condtion):
        Yaha par message dena chao to do ya nahi.

        if(condtion):
            your message.
        else:
            your message.
    else:
        default condition message.

Comparision conditional operations:

Note: Yaha par a aur b variable le kar example show kiya hai.

1. Equals: a == b
2. Not equals to: a != b
3. Less then: a < b
4. Less then or equal to: a <= b
5. Greater then: a > b
6. Greater then or equal to: a >= b
'''

a = 10
b = 10
c = 20

# single line condtion
if a > b:
    print('\na > b: Wali body me hain.')

# if else condtion
if a > b:
    print('\na > b: Wali body me hain.')
else:
    print('\nKoi bhi condtion sahi nahi nikli.')

# multipal condtion
if a > b:
    print('\na > b: Wali body me hain.')
elif b > c or b < c:
    print('\nelif b > c: wali body.')
    if a < c:
        if a > b:
            print('\na > b: Wali body me hain.')
        elif b > c or b < c:
            print('\nelif b > c: wali body.')
        else:
            print('\nKoi bhi condtion sahi nahi nikli.')
else:
    print('\nKoi bhi condtion sahi nahi nikli.')


# excersice

name = input('\nEnter your name: ')

if bool(name) == True:
    print('\nHi ' + name + ' welcome to condtion.')
else:
    print('\nAap name dena bhul gaye?')


# User se number lena hai aur check karna hai

num = int(input('\nEnter your lucky number: '))

if num > 20 and num < 25:
    print('\nYahoooo, you won the 1st prize.....')
elif num > 40 and num < 45:
    print('\nYahoooo, you won the 2nd prize.....')
elif(num > 12 and num < 15):
    print('\nYahoooo, you won the 3rd prize.....')
else:
    print('\nOhhhh, no pleas try again...')

'''
Question and Program:

1. input value ka type check karo ki kya aata hai?
'''