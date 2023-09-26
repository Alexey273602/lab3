import json

firm_profit_list = []
total_profit = 0

with open("firm_data.txt", 'r', encoding='utf-8') as file:
    for line in file:
        data = line.strip().split()
        firm_name = data[0]
        revenue = float(data[2])
        expenses = float(data[3])
        profit = revenue - expenses
        if profit > 0:
            firm_profit_list.append({firm_name: profit})
            total_profit += profit

average_profit = total_profit / len(firm_profit_list) if firm_profit_list else 0

average_profit_dict = {"average_profit": average_profit}
firm_profit_list.append(average_profit_dict)

with open("firm_profit.json", 'w', encoding='utf-8') as json_file:
    json.dump(firm_profit_list, json_file)

print("Данные о прибыли фирм и средней прибыли сохранены в файле firm_profit.json.")
