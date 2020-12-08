import csv
total_months = 0
total_volume = 0
net_profit = 0
net_profit_list = []
months = []
with open ('budget_data.csv') as csvfile:
    data_analytics = csv.reader(csvfile, delimiter= ",")
    data = next(data_analytics)
    jan_data = next(data_analytics)
    months.append(jan_data[0])
    total_months= total_months + 1
    total_volume = total_volume + int(jan_data[1])
    previous_pl=int(jan_data[1])
    for row in data_analytics:
        print(row)
        months.append(row[0])
        total_months = total_months + 1
        total_volume = total_volume + int(row[1])
        net_profit = int(row[1]) - previous_pl
        previous_pl = int(row[1])
        net_profit_list.append(net_profit)
        max_value = max(row[1])
        min_value = min(row[1])
        max_index = int(row[1].index(max_value))
        print(max_index)
        min_index = int(row[1].index(min_value))
        greatest_increase = max(row[1])
        greatest_decrease = min(row[1])
print("Budget Data")
print("Total Months:"+ str(total_months))
print("Total Volume:" + str(total_volume))
print(f"Average Change: {round(sum(net_profit_list)/len(net_profit_list), 2)}")
print("Greatest Increase in Profits: " + str(months[max.index(max(total_volume))+1]) 
      + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(months[min.index(min(total_volume))+1]) 
      + " " + "$" + str(greatest_decrease))

    