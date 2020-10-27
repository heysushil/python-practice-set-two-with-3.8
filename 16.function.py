'''
About Function in Python:

Function 2 type ke hote hain:

    1. pre-defined function
    2. user-defined function

Pre-defined function: 

1. Ye function programming lanaguage me pahle se define hote hain.
2. In work aur behaviour pahle se set hota hai.
3. Jaise ki example ke liye: print() function.
    a. print function python me output show karne ke liye use hota hai.
    b. Is funciton me number of aruments ka use kiya jata hai.
    c. Jaise ki print me hum direct math solve kar sakte hain.
    d. Koi dusra pre-define fucntion bhi use kar sakte hain. Jaise ki datatype check karne ke liye type() function.
4. Har pre-define fucntion ka work behaviour bilkul user-define function jaisa hi hota hai. Bas in funciton ko pahle se hi define kar diya gaya hai.
5. Jin funciton ya work behavious ko pahle se define nahi kiya gaya hai. Un ke liye hi hum user-define fucniton create karte hain.

User-defined function:

Note: funciton create karne ke liye 'def' keyword ka use karte hain.

1. User-define funciton ka name user define karta hai.
2. Funciton name hamesa relevent name hona cahiye. Taki name se function ka work behaviour pata chale.
3. Function ke sub types bhi hain:
    a. Function with arguments & with return value
    b. Function without arguments & without return value
    c. Function with arguments & without return value
    d. Function without arguments & with return value
4. Funciton ka work kisi bhi specific problem ko solve karne ke liye kiya jata hai.
5. Ek funciton ke andar aap multiple condtion, loops, function ya class tak call kar sakte hain.

Function ka syntax:

def your_function_name():
    funciton body

Funciton name ke limitations:

1. Fucntion name ko bhi create karte time varibale ke rules ko dhyan rakho.
2. Jaise new variable number se ya fir space se nahi start kar sakte ho. Same to same yaha par bhi wahi sare varaible ruls follow hote hain.

Note: Yaad rahe complete programming lanaguage me hame 2 chije bar bar milti hain.

1. Keywords: Jaise ke del, def, class etc...
2. Function: Jaise ki print(), if(), for() etc....

Function me argument aur return ka matlab:

1. Argument asal me ek simple varaibel jaisa hi hai. Jab bhi hum fucntion me argument ki baat karte hain. To iska matlab hota hai ki hum kuch varible ya values fucntion me recive kar rahae hain.
2. Because function me hum koi bhi ek specific work karte hain aur uska result show karate hain ya fir result ko return karte hain.
3. Jaise hamesa yaad rakho ki arguments ko funciton me recive hi kiya jayega. Waise hi jab bhi function koi work complete kar dega then yata result fucniton me hi show karado. Ya fir result ko return bhi karaya ja sakta hai.
4 Jab bhi bat result ko return karane ki ho, iska matlab hoga ki hum wo resutl funciton ke bahar recive karenge. Then usko kisi varibel me store kar sakte hain.

Static aur dynamic values ka matlab:

1. Static values means ye fix values hain jo hum ek bar define kar diye wahi rahega.
2. Dynamic values means jab hum user input ke through valeus recive karte hain use time user kuch bhi values de sakta hain.
'''

# b. Function without arguments & without return value

# defining funciton. yad arahe ye kewal funciton definition hai function ka use karne ke liye use call karna jaruri hai.
def userDetails():
    name = 'Debjit'
    course = 'Python'
    # store message on detail
    detail = '''
    Hi, my name is {} and I'm pursuing {} course.
    '''.format(name, course)
    # print the detail using print method
    print('\n', detail)

# call userDetails fuction
userDetails()


# c. Function with arguments & without return value

def userDetailsWithArguments(name, course):
    # store message on detail
    detail = '''
    Hi, my name is {} and I'm pursuing {} course.
    '''.format(name, course)
    # print the detail using print method
    print('\n', detail)

# call userDetails fuction
name = 'Mr. Debjit'
course = 'My Python'
userDetailsWithArguments(name, course)


# fucntion with list values
def funWithList(mylist):
    print('\nfunWithList:\n\nHi my name is ' + mylist[0] + ' and my course is ' + mylist[1])

mydata = ['debjit','python']
funWithList(mydata)

# recive values as list with useing * sign before argument name
# tupel(myval) dict()
def funReciveValuesAsDictinary(**mydictvalues):
    mydata = '''
    funReciveValuesAsList:

    Name: {}
    Course: {}
    Mobile: {}
    '''.format(mydictvalues['name'], mydictvalues['course'], mydictvalues['mobile'])
    print('\n', mydata)

name = 'Mr. Debjit'
course = 'My Python'
mobile = 997979879
funReciveValuesAsDictinary(name = name, course = course, mobile = mobile)


# d. Function without arguments & with return value
def fun_Without_Arg_But_With_Retrun_Value():
    name = 'Mr. Debjit'
    course = 'My Python'
    mobile = 997979879

    mydata = '''
    fun_Without_Arg_But_With_Retrun_Value:

    Name: {}
    Course: {}
    Mobile: {}
    '''.format(name, course, mobile)
    # print('\n', mydata)
    return mydata


result = fun_Without_Arg_But_With_Retrun_Value()
print(result)


# a. Function with arguments & with return value
def fun_with_arg_and_return_value(name, course):
    # store message on detail
    detail = '''
    fun_with_arg_and_return_value

    Hi, my name is {} and I'm pursuing {} course.
    '''.format(name, course)
    # print the detail using print method
    # print('\n', detail)
    return detail, name

# call userDetails fuction
name = 'Mr. Debjit'
course = 'My Python'
myresult = fun_with_arg_and_return_value(name, course)
print('\n', myresult)


