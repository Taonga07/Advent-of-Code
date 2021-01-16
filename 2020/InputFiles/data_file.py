import json, os

def GetFile(file):
    path = os.getcwd() + '/2020/InputFiles/'
    input_file = open(path + file + '.txt', 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data