'''
Dictionary in Python:

About Assosiative Array:

1. C, C++ ya php me hame assosiative array milta hai.
2. Synatx: variableName = array('name' => 'Sushil')
3. Assosiatve sysntax me array(key => value)
4. Yahi same concept of associative array python me Dictionary ke name se use hota hai.

Python me dictionary ko use karne ke liye:

1. Syntax: newvalue = {'key or userDefinedName' : 'value or userDefinedValue',}
2. Tupel me () small bracke ke agar koi single value define ki jaye to wo tuple type nahi hai because tuple ke liye last me comma dena jaruri hai.
3. Waise hi dictionay me {} ke andar key:value ke bad comma dena jaruri hai. Other wise same braket ka use set me bhi hota hai. Aur dono confilt ho jata hai.
'''

data = {}
print('\nData type: ', type(data))

# data = {key : value}
data = {'name' : 'Nikhil', 'mobile' : 987987987, 'course' : 'Python'}

print('\nName: ', data['name'])

profile = '''
--------------------------------
            {name}'s Profile
--------------------------------
Name: {name}
Mobile: {mobile}
Course: {course}
--------------------------------            
'''.format(name = data['name'],mobile = data['mobile'],course = data['course'])
# .format(data['name'], data['mobile'], data['course'])

print(profile)

# multi level dictionary
megadata = {
    'nikhil' : {
        'name' : 'Nikhil',
        'mobile' : 987987987,
        'course' : 'Python'
    },
    'debjit' : {
        'name' : 'Debjit',
        'mobile' : {
            'name' : 'Debjit',
            'mobile' : {
                'name' : 'Debjit',
                'mobile' : 9987987979
            }
        }
    }
}
print('\nMobile: ', megadata['debjit']['mobile'])

print('\nGet only keys: ', megadata.keys())
print('\nGet only values: ', megadata.values())
# print('\nPopitem: ', megadata.popitem())
print('\nPop: ', megadata.pop('nikhil'))

'''
Programms:

1. Apni profile dictinory ki madad se bana hai aur profile ka data mutliline string ka use karke show karna hai.

2. Multiple profiles sinle dictionary me bana hai. Is me se alag alag user ki detail multiline string ka use karke show karna hai. But yaha par sahi user ki profile single multiline stirng me hi banana hai.

3. Jo 2nd programm hai isme se ek kitne users the unko alag se dikhan hai.

4. Learn these methods: update() / setdefault() / values()
'''