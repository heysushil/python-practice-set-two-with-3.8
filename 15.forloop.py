'''
For loop ka work behavior:

1. For loop ka use kisi bhi sequacne ko print karne ke liye use hota hai.
2. Jaise ki hamare pas list, tuple, set and dictionary hai joki values ko sequence me dete hain.
3. Jaise ham ek example lete hain aur use print karke check karte hain.

For loop ka syntax:

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
'''

friendlist = ['nikhil', 'sushil','nikhil', 'sushil']
# friendlist = []

for name in friendlist:
    print(name)

# range(stopvalue) | range(start, stop)
for i in range(1, 11):
    print(i)

# range(start, stop, diffrence)
print('\n')
for i in range(2, 21, 2):
    print(i)

