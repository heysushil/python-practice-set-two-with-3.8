'''
Set in python:

Important points to set:

1. Set ko {} is braket se denote karete hain.
2. Set values ka koi order nahi hota hai. Means values ko agar index position ke behalf par feach karna caho to error milega.
3. Set me values hamesa unique honge.
4. Set values hamesa suffle karte rahete hain.

Set ka use collection of set me se dublicacy remove karne ke liye kiya jata hai.

Set ka use ek se jada set ko apas me mager karn ke liye aur sath me dublicate valeus ko filter karne ke liye kiya jata hai.
'''

# set
myset = {1,4,53,5,6,8,5,4,3,5,6}
print('\Myset: ', type(myset))
print('\nmyset: ', myset)

# createing set
set_a = {1,4,53,5,6,8,5,4,3,5,6}
set_b = {3,4,5,6}
set_c = {11,33,55,66}


# union
union_of_a_c = set_a.union(set_c)
print('\nunion_of_a_c: ', union_of_a_c)

intersect = set_a.intersection(union_of_a_c)
print('\nset_a.intersection(union_of_a_c): ', intersect)

s1 = {'a','b','c','d'}
s2 = {'a','b','e','r','y'}
s3 = {'e','r','y'}
myunion = s1.union(s2)
print('\nremove dublicay: ', myunion)

diff = s1.difference(s2)
print('\nCheck diffrecne b/t s1 and s2: ', diff)

s2.difference_update(s1)
print('\nUpdate dirrerence: ', s2)
print('\ns2: ', s2)

s2.discard('r')
print('\nafter discard s2: ', s2)

print('\ncheck superset: ', s3.issuperset(s2))
print('\ncheck subset: ', s2.issubset(s3))

