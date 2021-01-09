import json, os

path = os.getcwd() + '/InputFiles/'
input_file = open(path + 'Input 1.txt', 'r')
input_data = input_file.read()
input_file.closed
data_list = input_data.split()

for value in data_list:
    for value1 in data_list:
        check = int(value)+int(value1)
        if check == 2020:
            print(value, value1)
            print(int(value) * int(value1))