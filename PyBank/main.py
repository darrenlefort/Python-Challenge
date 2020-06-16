import csv
import os

pathway = os.path.join("Resources", "PyBank_data.csv")

with open (pathway) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile, None)
    print(f"Header: {csv_header}")


txt_header = "Financial Analysis"

output_path = open("analysis/PyBank_analysis.txt", "w")
output_path.writelines(txt_header)
output_path.close()