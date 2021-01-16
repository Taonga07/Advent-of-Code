import InputFiles.data_file as file

input_data = file.GetFile('Input1')
data_list = input_data.split()

for value in data_list:
    for value1 in data_list:
        if int(value)+int(value1) == 2020:
            print(f'The two entries that\'s sum is 2020 are: {value} and {value1}')
            print(f'Multiplied together they make: {int(value) * int(value1)}')
            raise SystemExit