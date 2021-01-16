import InputFiles.data_file as file

input_data = file.GetFile('Input1')
data_list = input_data.split()

for value in data_list:
    for value1 in data_list:
        for value2 in data_list:
            if int(value)+int(value1)+int(value2) == 2020:
                print(f'The three entries that\'s sum is 2020 are: {value}, {value1} and {value2}')
                print(f'Multiplied together they make: {int(value) * int(value1) * int(value2)}')
                raise SystemExit