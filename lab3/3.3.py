def delete_brackets(string):
    for letter in string[::-1]:
        if not letter.isdigit():
            string = string[:-1]
        else:
            break
    return string


with open("Учёба.txt", 'r', encoding='utf-8') as study:
    lines = study.readlines()
    list = []
    for line in lines:
        list.append(line.split())
    for line in list:
        line[0] = line[0][:-1]
    for line in list:
        for i in range(1, len(line)):
            line[i] = delete_brackets(line[i])
    keys = []
    values = []
    diction = {}

    for line in list:
        value = 0
        for i in line:
            if i.isnumeric():
                value += int(i)
            else:
                keys.append(i)
        values.append(value)
    diction = dict(zip(keys, values))
    print(diction)
