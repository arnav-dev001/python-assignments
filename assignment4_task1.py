# the program tries to read and print the file
try:
    file = open('assignment4task1.txt', 'r')
    read_file = file.readlines()
    
    # prints the file
    print('Reading file content: \nLine 1: ' + read_file[0] + 'Line 2: ' + read_file[1])
except:
    # if file was not found, this error
    print("Error: The file \'assignment4task1.txt\' was not found")
