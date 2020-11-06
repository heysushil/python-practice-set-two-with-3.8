'''
File handling kya hai? Kya work hota hai?

1. file handling normal jaise hum system me files create karte hai. Wahi same work hum python ke help se karenge.
2. EK file ke case me hum:
    1. file ko create karna
    2. file ko read karna
    3. file ko update karna
    4. file ko delete karna

File handling ka work:

1. File handling me 4 methods mostly use hote hain:
    1. open()
    2. read()
    3. write()
    4. close()
2. Sab se pahle hum file ko open karte hain. Is case me file open karne ke sath kuch methods use karne hote hain:
    1. open() method me second argement as 4 alag tarike ke arguments pass kar sakte hain:
        1. 'r': file read ke liye, error if file not exists
        2. 'a': append - create file if not exists
        3. 'w': open file for write, create file if not exists
        4. 'x': create file, if file exists get error
    2. open() method me 2 aur arguments milte hian:
        1. 't': text - ye by default text mode ke liye hota hai
        2. 'b': binary - multimedia format (e.g: image)
'''

# creating a new file

# use open method to creat a file and add some data
new_file = open('file_handling/files/demo.txt', 'w')

# print this file to check is it open or not
print('\nDemo file: ', new_file)

# add number of data on demo file
# Always remeber that 'w' mode alway rewrite the file
data = 'Always remeber that mode alway rewrite the file'
new_file.write(data)

# close new file
new_file.close()

# function to create new file
def create_file_to_append_data():
    filename = input('\nEnter file name: ')

    # open file
    myfile = open('file_handling/files/'+filename+'.txt', 'a')

    # add data on this file
    user_message = input('Enter your message: ')

    # add message to file
    myfile.write(user_message)
    print('\nYour message is added on ' + filename + '.txt  file.')

    # finally close the file
    myfile.close()

# call funciton
# create_file_to_append_data()

# read existing file
def read_file():
    # get file name by user
    filename = input('\nEnter file name: ')

    # open file on read mode
    myfile = open('file_handling/files/'+filename+'.txt', 'r')

    print('\nMyfile: ', myfile.read())
    # myfile.
    myfile.close()

# call read file
read_file()

'''
Try these methods:

1. check all read realted methods thier works?
2. check alll write realted methods and thier works?
'''

'''
Problems need to fix:

1. read_file() funciton me agar file pahle se exist nahi karti hain then error milta hain usko handel karo.

2. Is tarikese baki funciton me aane wale error ko find karke handle karo?
'''