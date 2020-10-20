'''
Python me Loop ka use and work case.

Python me hame 2 loop case milte hain.

1. while loop
2. for loop

Note: Waise other programming languages like C, C++, PHP me hame 3 loop case milte hain. For, while, do-while. Also C, C++ jaise lanagauge me increment (++) aur decrement (--) use hota hai but python me ye use nahi hota hai.

Loop ka use kyo karte hain?

1. Loop same type ke repated work ke liye use hota hai.
2. Sequence datatype - list, tuple, range ye values ko index form me sotore rakhte hain. Inka use loop me values ko one by one print karne ke liye kiya ja sakta hai.
3. Ya fir kisi bhi collection of data like database table data ko bhi hum loop ke through print kara sakte hain.
4. Loop me pre aur post increment aur decrement hote hain.

While loop ka syntax:

intilization
while (condtion):
    body of while loop
    increment or decrement

While loop syntax ke baare me:

1. Intilization me koi bhi starting point decide karna hota hai. Like i = 1, Becasue loop ko hamesa starting and ending point ki need hoti hai.
2. while (i <= 10): Ye condtion hogi ki loop ko kaha tak chalna hai.
3. While body: yaha par jo kuch bhi print karna hai ya fir koi loop ya condtion chalana hai. Wo sab kuch yaha par kiya ja sakta hai.

For loop syntax:

for intilization in collectionOfValues:
    body of for loop

For loop syntax ke baare me:

1. For loop me intilization kewal variable ka hoga isme koi bhi value assign nahi karna hai. Becasue jo collection values hai usme se one by one values intilization ko recive hoga and wo usko for loop ke body ko pass karega.
2. Collection of values: Ye koi bhi collection ho sakta hai. Like as:
    a. list collection
    b. tuple collection
    c. range collection
    d. database tabel data collection
    e. so on....

If aur while loop me difference?

1. If Condtion agar sahi hai to wo condtion body me aayega aur wahi work stop ho jayega.
2. While loop me jab tak condtion sahi hai tab tak loop chalta ranega.
'''

# i ye ek starting point hai jo ye bata raha hai ki loop 2 se start hoga.
i = 2
# ye while ki condtion hain jaha par ye condtion lagaya hai ki, i jab tak chota ye equal to hoga 100 ke tab tak loop chalega
while i <= 100:
    '''
    Yaha par i jo hai ye tab tak loop se bahar nahi nikalne dega jab tak i ki value 100 ke equal na ho jaye.
    That means ki, loop tab tak repeate hoga jab tak condtion sahi rahe gi.
    while loop body me print(i), i ki value print kar raha hai jo bar bar increment ho kar mil raha hai
    '''
    print(i)
    # loop ke andar hum condtion laga sakte hain, aur condtion ke andar break ka use karke loop ko waha par condtion ki mad se rook sakte hain.
    if i == 20:
        break
    # ++ --: i += 2 ye asal me i = i + 2
    i += 2


# create friend party list
frind_num = int(input('\nEnter number of friends: '))

friend_list = []
i = 0
while i < frind_num:
    i += 1
    name = input('Enter friend name: ')

    # stop debjit
    if name == 'debjit':
        print('\n' + name + ' you are not allowed.')
        # break
        continue

    friend_list.append(name)

    # i += 1

print('\nFinal friend list: ', friend_list)




'''
Questions:

1. Do_while loop kya hai?

While loop programs:

1. 1 to 10 Number print karna hai.

2. 1 to 50 number print karna hai but jab 25 number mile to hame ek alg print message show karn hai 25 numbre ke liye using condtion.

3. Ek list create karo aur usme apne friedns ka name include karo then agar first friend aaye to usko hello hi message show karna hai. Second friend aaye to usse colleage ke bareme puchna hai. Thired fried aaye to susse jo man kare wo puch lena. Yaha par multiple condtion ka use karna hai. Sath me isme sabhi friend ko while loop karne ke show karn hai.

4. Ek list create karna hai jisme ki alphabets honge aur unko while loop ka use karke print karna hai but jab bhi koi vovel aaye to usko batan hai. Yaha par while loop and condtion use hoga. Yaha par single if condtion me ye kaam karna hai iske liye multiple condtion nahi use karna hai.

5. Jis tarike se list me values ko append kiya gaya hai, waise hi ek dictinaory banai hai aur usem ek single use ki details ko add karna hai aur last me multi line stirng ka use karke value show karna hia. 

Jaise ki: name, email, mobile, address, course

6. Ek main list bana hai jisme 4 alag lsit add honge, means ye 4 list 4 alag party me anne wale friend ki list hai. Jisko ek main list me add karna hai iske liye extend ka use hoga.
'''
