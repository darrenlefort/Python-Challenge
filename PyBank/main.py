import csv
import os

pathway = os.path.join("Resources", "PyBank_data.csv")

dates = []
profit = []
loss = []

with open (pathway) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile, None)
    print(f"Header: {csv_header}")

    sum_profit = 0.0
    for row in csvreader:
        dates.append(str(row[0]))
        sum_profit = row[1]
        if int(row[1]) > 0:
            profit.append(int(row[1]))
        else:
            loss.append(int(row[1]))
    
        

total_months = str(len(dates))
average_change = str(int(sum_profit) / int(total_months))
max_increase = max(profit)
max_loss = min(loss)

txt_header = "Financial Analysis"
total_months = str(total_months)
txt_lines = [
    [txt_header], 
    ["---------------------------"], 
    ["Total Months: " + total_months], 
    ["Total: $" + sum_profit], 
    ["Average Change: $" + average_change], 
    ["Greatest Increase in Profits: " + str(max_increase)], 
    ["Greatest Decrease in Profits: " + str(max_loss)]]

for s in txt_lines:
    print(*s)


output_path = open("analysis/PyBank_analysis.txt", "w")
output_path.write(txt_header)
output_path.write("\n") 
output_path.write("---------------------------")
output_path.write("\n") 
output_path.write("Total Months: " + total_months)
output_path.write("\n") 
output_path.write("Total: $" + sum_profit)
output_path.write("\n") 
output_path.write("Average Change: $" + average_change)
output_path.write("\n") 
output_path.write("Greatest Increase in Profits: " + str(max_increase))
output_path.write("\n")  
output_path.write("Greatest Decrease in Profits: " + str(max_loss))
output_path.close()