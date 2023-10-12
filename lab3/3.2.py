with open("Клиенты банка.txt", 'r', encoding='utf-8') as clients:
    lines = clients.readlines()
    list = []
    for line in lines:
        list.append(line.split())
    sum = 0
    for i in list:
        if i[1] == '0':
            print(f"{i[0]} имеет 0 на счету")
        else:
            sum += int(i[1])
    print(f"\nОбщая сумма всех вложений клиентов банка: {sum}")
