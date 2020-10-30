'''
Inheritance Kya hai?

1. Inheritance ek concept hai jiski madad se hum code ko reuse kar sakte hain.
2. Inheritance OOP's (Object Oriented Programming) ka concetp hai to iska matalb hai ki hum iska use class ke sath hi karenge.
3. Inheritance ek class ke code ko kisi bhi dusre class me use karne ki facility deta hai.
4. Inheritance me hame 2 tarike milte hain:
    a. mutlilevel inheritance
    b. mutlipal inheritance
5. Inheritance me hame 2 tarike ki class milti hain:
    a. parent class: Ye class jiske ke pas sare concept hai.
    b. child class: Ye class jo parent class ke concepts ka use karegi.
6. Inheritance ko asani se samjhne ke liye ise hum kuch is tarike se samjh sakte hain ki:
    a. parent class: dendata (dene wala)
    b. child class: lendata (lene wala)

Multilevel inheritance kya hai?

1. Multilevel inheritance ka use class me ek chaine form me hota hai. Jaie ki a frined hai b ka, b friend hai c ka, c friend hai d ka. Then d indirectly friend hogaya a ka.
2. Yahi same concept multilevel inheritance me use hota hai.
3. Multilevel inheritance me hamesa koi bhi child class kewal single parent class ki properties ko inherit ya use karega.
4. Agar ek child class ek se jada parent class ka use karta hai then is concetp ko 'multiple inheritance kahenge'.

Multiple inheritance kya hai?

1. Yaha par ek child class ek se jada parent class ki properties ka use karta hai.
2. Iske alawa baki multilevel jaisa hi concpet hota hai.
'''

# Parent class
class Calculater:

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

# Personal Info parent class
class MyData:
    def __init__(self, name, course):
        self.n = name
        self.c = course

    def mydetails(self):
        print('\nHi my name is ' + self.n + ' and I learning ' + self.c)


# child class: yaha par parent class ko inherit karna hai
class MyKhata(Calculater, MyData):
    # parent class ke constructer ko child class ke constructer se 1 aur b pass kiya jayega.
    def __init__(self, a, b, name, course):
        # Pass value by class name
        Calculater.__init__(self, a, b)
        MyData.__init__(self, name, course)

        # Use super keyword to pass values to parent class constructer
        # super().__init__(a, b)

    def kharcha(self):
        mykharcha = Calculater.add(self)
        MyData.mydetails(self)
        print('\nMere course ki fee: Rs.', mykharcha, '/- hai.')

# child class object
mykhata_obj = MyKhata(20, 20, 'Nikhil', 'Python')

mykhata_obj.kharcha()

# Parentclass objcet
# parentObj = Calculater(20, 20)
# print('\nCalculater sum: ', parentObj.add())
