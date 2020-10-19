'''
Python Tuple:

1. Tuple nonchange hai, aur list changeable hai. iska systax ()
2. Tuple me values na change kar pane ki wajah se isme is tarike ke koi bhi methods nahi milte hai.
3. Single value wale tuple me value ke sath ek comma dena jaruri hai otherwiese wo ek stirng ya int value hi hoga.
4. List ke jaise hi tuple me same to same slicing follow hota hai. Ye posstive and negative dono me hota hia.

Tuple me total 2 mehtods milte hain:

Note: Example tuple - newtuple = (11,22,33,33)

1. count(): Same list count() method jaisa hi hai. Is ke use se tuple me exist dublicate values ko count kiya jata hai. Example: newtuple.count(33)
2. index(): Same list index jaisa hi hai. Tuple me kisi bhi value ka index posstion find karne ke liye index method ka use kiya jata hai. Example: newtuple.index(33)
'''

# new tuple
mytuple = ('nikhil','debjit','sushil','debjit','python','debjit')
print('\nmytuple type: ', type(mytuple))
print('\nmytuple: ', mytuple)

# related mehtods
print('\nIndex of python: ', mytuple.index('python'))
print('\nCount debjit: ', mytuple.count('debjit'))

# slicing
print('\nget index vlaue: ', mytuple[2])
print('\nOnly start: ', mytuple[2:])

# find length
print('\nFind mytuple length: ', len(mytuple))
print('\nFInd nikhil length: ', len('nikhil'))

# convert tuple into list for change or update
getTupleDataInList = list(mytuple) 
print('\nType getTupleDataInList: ', type(getTupleDataInList))

# add 2 more canditates
getTupleDataInList.append('Raju')
getTupleDataInList.append('Reena')

# add bunch of students
newstudents = ['Hari','Ram','Seema','Pehu']
getTupleDataInList.extend(newstudents)

getTupleDataInList.remove('nikhil')
getTupleDataInList.remove('debjit')
print('\ngetTupleDataInList: ', getTupleDataInList)
print('\nGet last index: ', getTupleDataInList[-1])


# change list into tuple again
mytuple = tuple(getTupleDataInList)
print('\nCheck type of mytuple: ', type(mytuple))

print('\nmytuple: ', mytuple[0])

invitationCard = '''
--------------------------------------------
            Invitation Card
--------------------------------------------
1: {}
2: {}          
'''.format(mytuple[0].capitalize(), mytuple[1].upper())

print(invitationCard)

'''
HM:
1. Jaise list me index values find kiya tha waise hi yaha tuple me karna hai.
2. Jaise index ki slicing ki thi ex: [0:2] yahi same kaam tuple me karna hai.
3. Jaise list me negative slicing ki thi waise hi same yaha karna hai.

4. tuple ka use karke 2 list create karna hai:
    1. first list me party me aane wale friends ka name add karna hai
    2. second list me party me naa aane wale friedns ka name add karna hai

    Then:
    1. Kuch friends jo second list me the unme se 2 friend party me aane ke liye taiyar hain. Unko first list me add karna hai.
    2. First list me 3 friend ayse hain jo nahi aa payenge. Unko first list se nikal kar second list me add karna hai.
    3. Last me jo log party me aane wale hain un sabhi ko mila kar ek multiline string ka use kar ke invitation bana hai.
    4. Jo log party me nahi aa sakte hain unke liye bhi ek multi line sting ka use karke message bana hai.
'''

