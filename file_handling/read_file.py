import os

# if os.path.exists('file_handling/files/demo.txt') == True:
#     print('\n I got the file')
#     os.rename('file_handling/files/demo.txt', 'file_handling/backup/demo.txt')

# exit
# choose_file_for_read()
def choose_file_for_read():
    pass

# choose_to_write_in_file()
def choose_to_write_in_file():
    filename = input('\nEnter file name: ')

    # open file
    myfile = open('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/'+filename+'.txt', 'a')

    # add data on this file
    user_message = input('Enter your message: ')

    # add message to file
    myfile.write(user_message)
    print('\nYour message is added on ' + filename + '.txt  file.')

    # finally close the file
    myfile.close()

    user_options()

# Provide option to user for read and write:

def user_options():
    message = '''
    ------------------------------------------
                Hello User
    ------------------------------------------
    Choose available options:
    
    1. Choose File for Read
    2. Choose to write in available file
    3. Exit
    -------------------------------------------
    '''
    print(message)

    try:
        options = int(input('Enter numbre to visist available options: '))
    except:
        print('\nOnly numbers allowed. Try again with number.')
    else:
        if options == 1:
            choose_file_for_read()
        elif options == 2:
            choose_to_write_in_file()
        elif options == 3:
            print('\nYou are successfully exit.')
        else:
            print('\nYou entered wrong options. Try again.')

user_options()