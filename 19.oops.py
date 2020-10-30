'''
Class ke bare me jankari:

1. Class ko use karne ke liye 'class' keyword ka use kiya jata hain.
2. Jaise fucntion me function ko use karne ke liye fucntion call karte hain waise hi yaha par class ko use karane ke liye 'object' banate hain.
3. Jaise single function me ek kisi work ko complete kiya jata hai. Wise hi class multiple functions aur  attributs or variables ka collection hota hai.
4. Jaise normal case me hum ek fucntion ko function kahte hain. Wise hi ek function class me as a 'method' kaha jata hain.
5. Hum class me variables ko 'attributs' kahte hain.

Note: Class ka first character hamesa capital letter me hona cahiye.
'''

# calculater: fucntion definetion
def add(a, b):
    return a + b

# subtract funciton
def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

# call add function
myadd = add(10, 20)
print('\nAdd: ', myadd)
print('\nSub: ', sub(20, 10))
print('\nMul: ', mul(10, 20))


# create class of calculater
class Calculater:
    # class constructer: __init__() ye ek special method hota hai
    # constructer me hamesa ek 'self' arguemtn ayega hi ayega. ye har ek argument ka current instance banata hai. Jiski madad se hum class me available har ke method ko same values pass kar sakte hain.
    def __init__(self, a, b):
        # yaha par a aur b 2 arguement recive hue hain.
        # inka instace create karna hai
        self.num1 = a
        self.num2 = b

    # calculater: fucntion definetion
    def add(self):
        return self.num1 + self.num2
        # pass

    # subtract funciton
    def sub(self):
        return self.num1 + self.num2
        # pass

    def mul(self):
        return self.num1 + self.num2
        # pass

# Jiase function ko call kiya jata hai waise hi class ka object create karate hain.

mycalculater = Calculater(20, 10)

# call add method of mycalculater object
print('\nNum1: ', mycalculater.num2)
print('\nMyAdd: ', mycalculater.add())
print('\nMySub: ', mycalculater.sub())
print('\nMyMul: ', mycalculater.mul())



# Class constructer ko value na de kar direct method ko value pass karna hai?

class My_method_values:
    def __init__(self):
        pass

    # method for mydetails
    # Ye single argumetn recive karne ke liye hai
    # def mydetails(self, name):

    # ye multipal values ko as a tuple recive karne ke liye hai
    # def mydetails(self, *name):

    # ye mutlpal key values ko dictionary form me recive karen ek eliye hai
    def mydetails(self, **name):
        print('\nHi my name is ', name)

# create object
mydata = My_method_values()

# call mydetails method
mydata.mydetails(name = 'Nikhil', myname = 'hey sushil', yourname = 'debjit')


'''
Question:

1. Class ke andar 4 fucntion work behaviour ke liye fucntion create karne hai apne hisab se aur unka result dekhna hai:

    a. Function without arguments & without return value
    b. Function with arguments & without return value
    c. Function without arguments & with return value
    d. Function with arguments & with return value

2. Ek class banana hai Restorant name se aur iske andar alag-alag disess ke liye fucntion create karne hai aur unme apne hisab se print message use kanr hai.
'''