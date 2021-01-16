data_list = []
new_passwords, passwords = 0, 0

input_file = open('2020/InputFiles/Input2.txt', 'r')
for line in input_file.readlines(): 
    a, b, c = line.rstrip().split(' ')
    data_list.append([a, b, c])
    #####PART 1#####
for item in data_list:
    pos1, pos2 = item[0].split('-')
    count = item[2].count(item[1])
    if int(pos1) <= count <= int(pos2):
        passwords += 1
    letters = item[2]
    #####PART 2#####
    if letters[int(pos1)-1] == item[1]:
        if letters[int(pos2)-1] != item[1]:
            new_passwords += 1
    elif letters[int(pos2)-1] == item[1]:
        new_passwords += 1

input_file.closed
print(f'Total amout of correct password: {passwords}')
print(f'Total amout of new correct password: {new_passwords}')