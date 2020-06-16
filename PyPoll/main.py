import csv
import os

pathway = os.path.join("Resources", "PyPoll_data.csv")

with open (pathway) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile, None)
    print(f"Header: {csv_header}")

    
txt_header = "Election Results"

txt_lines = [
    [txt_header], 
    ["---------------------------"], 
    ["Total Votes: "], 
    ["---------------------------"], 
    ["Winner Name: "], 
    ["2nd Place Name: "], 
    ["3rd Place Name: "], 
    ["4th Place Name: "], 
    ["---------------------------"], 
    ["Winner Name: "], 
    ["---------------------------"]
]

for s in txt_lines:
    print(*s)
   
output_path = open("analysis/PyPoll_analysis.txt", "w")
output_path.write(txt_header)
output_path.write("\n") 
output_path.write("---------------------------")
output_path.write("\n") 
output_path.write("Total Votes: ")
output_path.write("\n") 
output_path.write("---------------------------")
output_path.write("\n") 
output_path.write("Winner Name: ")
output_path.write("\n") 
output_path.write("2nd Place Name: ")
output_path.write("\n")  
output_path.write("3rd Place Name: ")
output_path.write("\n")  
output_path.write("4th Place Name: ")
output_path.write("\n")  
output_path.write("---------------------------")
output_path.write("\n") 
output_path.write("Winner Name: ")
output_path.write("\n")  
output_path.write("---------------------------")
output_path.write("\n") 
output_path.close()