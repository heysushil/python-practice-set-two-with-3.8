import os

def delete_file_with_backup():
    # get file name by user which he/she want's to delete
    file_name = input('\nEnter file name which you want to delete: ')

     # check file exists or not
    existing_path = 'D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/files/'+ file_name + '.txt'

    if os.path.exists(existing_path) == True:
        # Take backup of file which you want to delete
        destination_path = 'D:/xampp/htdocs/htmldemo/python-practice-set-two-with-3.8/file_handling/backup/'+ file_name + '.txt'

        print('\nCheck bakup response: ', os.rename(existing_path, destination_path))

        print('\nCongratulations, Your file ' + file_name + ' successfully deleted.')

    else:
        print('\nYour file '+file_name+' does not exists. Try again with right file.')

delete_file_with_backup()