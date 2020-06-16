import csv
import os

pathway = os.path.join("Resources", "PyBank_data.csv")

with open (pathway) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile, None)
    print(f"Header: {csv_header}")


txt_header = "Financial Analysis"

txt_lines = [
    [txt_header], 
    ["---------------------------"], 
    ["Total Months: "], 
    ["Total: $"], 
    ["Average Change: $"], 
    ["Greatest Increase in Profits: "], 
    ["Greatest Decrease in Profits: "]]

for s in txt_lines:
    print(*s)


output_path = open("analysis/PyBank_analysis.txt", "w")
output_path.write(txt_header)
output_path.write("\n") 
output_path.write("---------------------------")
output_path.write("\n") 
output_path.write("Total Months: ")
output_path.write("\n") 
output_path.write("Total: $")
output_path.write("\n") 
output_path.write("Average Change: $")
output_path.write("\n") 
output_path.write("Greatest Increase in Profits: ")
output_path.write("\n")  
output_path.write("Greatest Decrease in Profits: ")
output_path.close()