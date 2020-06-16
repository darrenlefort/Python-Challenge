import csv
import os

pathway = os.path.join("Resources", "PyPoll_data.csv")

with open (pathway) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile, None)
    print(f"Header: {csv_header}")

    
txt_header = "Election Results"
    
output_path = open("analysis/PyPoll_analysis.txt", "w")
output_path.writelines(txt_header)
output_path.close()