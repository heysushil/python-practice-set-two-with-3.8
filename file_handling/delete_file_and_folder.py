# create new file
# filename = input('/nEnter file name: ')
# open file
# Folder path ke liye vscode me use folder par right click karke copy path otpion par click karo. so us folder ka path copy ho jayega. 
filename = input('\nCreate new filename: ')
myfile = open('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/'+ filename +'.txt', 'a')

print('\nCheck myfile outptut: ', myfile)
myfile.close()

'''
------------------ Delete File -------------------
'''

import os

# direct remove file
# os.remove('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/mydemo.txt')


delete_file_name = input('\nEnter file name for delete: ')

# remove but before check FileNotFoundError
checkfile = os.path.exists('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/'+ delete_file_name + '.txt')

if checkfile == True:
    os.remove('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/'+ delete_file_name +'.txt')
else:
    print('\n',delete_file_name + ' file not exists. Try with other file name.')

'''
------------------ END Delete File -------------------
'''

'''
------------------ CREATE NEW FOLDER -------------------
'''

folder_name = input('\nCreate new folder name: ')
os.mkdir('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/' + folder_name)

'''
------------------ END CREATE NEW FOLDER -------------------
'''

'''
------------------ DELETE FOLDER -------------------
'''

folder_name = input('\nDelete folder name: ')
os.rmdir('D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/' + folder_name)
