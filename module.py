'''
Module kya hai? Ya libray kya hai? Ya file ko reuse kaise karte hain?

1. Module asal me python programming me ek python file hai. Jis ke andar number of classes, function, methods, argumetns ho sakte hain.

Moduel Kaise use kare?

1. Iske liye 'import' keyword ka use kiya jata hai.
2. Particular class, argument ko get karne ke liye 'from' keywork ka use karte hian.
3. Module ya file name log nahi useko sort form me alias bane ke liye 'as' keywork ka use kiya jata hai.
'''

# import full file
# import myclass as m

# import specific class
from myclass import Calculater as m

# m.add(10, 20)

# myobj = m.Calculater(20, 50)
myobj = m(20, 50)
print('\nClass add: ', myobj.add())