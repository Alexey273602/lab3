with open("F1.txt", 'w') as F1_obj:
    while F1_obj.write(input("Введите строку\n")):
        F1_obj.write('\n')
with open("F1.txt", 'r') as F1_obj, open("F2.txt", 'w') as F2_obj:
    for line in F1_obj:
        if not any(char.isdigit() for char in line):
            F2_obj.write(line)
with open("F2.txt", 'r') as F2_obj:
    lines = F2_obj.readlines()
    if lines:
        last_line = lines[-1]
        words = last_line.split()
        word_count = len(words)
        print(f"Количество слов в последней строке файла F2: {word_count}")
    else:
        print("Файл F2 пуст.")