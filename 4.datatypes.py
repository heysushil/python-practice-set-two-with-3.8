'''
Data Types:

1. str: string = Ye Alphabets hote hain. ' " """
2. Numeric Types: Ye sabhi number accept karene wale datatype hain
    a. int: integer = Ye positive aur negative dono hi number accept karta hain. Example: a = 10 | a = -10
    b. float: float = Iska use point number ke liye hota hai. Example: a = 10.10 | a = -10.10
    c. complex: complex = j . Isme hame kisi bhi int ya float value ke sath small j use hua ho to wo complex number hai. Example: a = 10j | a = 10.10j

3. Sequence Type:
    a. list: List changeable hai. List Box []
    b. tuple: Non-Changable. Tuple Box ()
    c. range: Ye ek method hai aur isme (start,end)
4. Mapping Type:
    a. dict: dictinary box {key:value}
        Example: {'name':'python'}
5. Set Type: union etc...
    a. set: box {}
        Example: {0,9}
6. Boolean Type: True | False
7. Binary Type: bytes, bytearray, memoryview

Array Syntax: Note: It's not part of Python
    Index array => data = array[1,2,3,4]
'''

# string values
name = 'Hello Debjit007, how are you? '
print(name)

name = '''
Extra Study:

    1. What is array and index array?
    [11,22,33,44]
    0  1  2  3
    2. What is associative array?
    3. What is object?
    4. What is the difference b/t list, tuple, dict and set
'''
print(name, type(name))

# number types this_is_my_firs_varaibal
intergerNumber = 100
typeOfInterNumber = type(intergerNumber)
print(intergerNumber, typeOfInterNumber)

floatNumber = 11.11
print(floatNumber, type(floatNumber))

complexNumber = 11j
print(complexNumber, type(complexNumber))

# sequeacne
listValues = [1,2,3,4,5,6,7]
print(listValues, type(listValues))

tupleValues = (1,2,3,4,5,6,7)
print(tupleValues, type(tupleValues))

# dictionary
dictionaryValues = {'name':'Python langauge'}
print(dictionaryValues, type(dictionaryValues))

# set
setValues = {0,2,3,4,5,6,7}
print(setValues, type(setValues))

# bool
booleanValue = bool(setValues)
print(booleanValue)


'''
Extra Study:

1. What is array and index array?
[11,22,33,44]
  0  1  2  3
2. What is associative array?
3. What is object?
4. What is the difference b/t list v/s tuple and dict v/s set
'''
