# create file to store list of all creating files

# create new file with adding file name in file
def create_file():
    # get file name by user
    filename = input('\nCreate new filename: ')
    
    # add file name in list_of_files
    myfile = open('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/list_of_files.txt', 'a')
    myfile.write(filename+'\n')

    # time to also create a file with provided name
    myfile = open('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/'+ filename +'.txt', 'w')

# create_file()

# show available files name as option to user
def show_all_files():
    myfile = open('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/list_of_files.txt', 'r')

    # get all available data of file in list
    file_names_in_list = myfile.readlines()
    # print('\n', file_names_in_list)
    final_list = []
    print('\n')
    i = 1
    for r in file_names_in_list:
        print(i, r.strip())
        # append data with strip method to remov \n
        final_list.append(r.strip())
        i += 1
    
    option = int(input('\nEnter your options: '))
    print('\nOption: ', option)
    # myfilename = final_list[option-1]
    print('\nFinal list: ', final_list[option-1])

show_all_files()

'''
Next work:

1. Option show hone ke bad user agar koi bhi option enter kare then use option ke file ko append mode me open karna hai.

2. THen use ko message show karo this file open for write your message. Enter your message.

3. Message enter karne ke bad user ko sucess ka message show karo. Then usne jo bhi message add kiya wo message show karo.

4. Then user to again files ka option show karo ki:
    1. Choose file to enter your message
    2. Choose your recent file - Ye just previouse file ko hi open karn hai ki user usi file me aur meesage add karna chata hai uske liye.
    3. Exit

'''