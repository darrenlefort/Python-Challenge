import csv
import os

pathway = os.path.join("Resources", "PyPoll_data.csv")

candidate = []
candidate_votes = {}
total_votes = 0
winning_count = 0
winning_person = ""
winning_percent = 0
second_count = 0
second_person = ""
second_percent = 0
third_count = 0
third_person = ""
third_percent = 0
fourth_count = 0
fourth_person = ""
fourth_percent = 0

with open (pathway) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile, None)
    print(f"Header: {csv_header}")

    for row in csvreader:  
        name = row[2] 
        total_votes += 1
        if name not in candidate:
            candidate.append(name)
            candidate_votes[name] = 0
        candidate_votes[name] = candidate_votes[name] + 1
# Python sorts dictionaries automatically
print(candidate_votes)

winning_count = str(list(candidate_votes.values())[0])
winning_person = list(candidate_votes)[0]
winning_percent = str(round(((int(winning_count) / total_votes) * 100), 0))

second_count = str(list(candidate_votes.values())[1])
second_person = list(candidate_votes)[1]
second_percent = str(round(((int(second_count) / total_votes) * 100), 0))

third_count = str(list(candidate_votes.values())[2])
third_person = list(candidate_votes)[2]
third_percent = str(round(((int(third_count) / total_votes) * 100), 0))

fourth_count = str(list(candidate_votes.values())[3])
fourth_person = list(candidate_votes)[3]
fourth_percent = str(round(((int(fourth_count) / total_votes) * 100), 0))

txt_header = "Election Results"

txt_lines = [
    [txt_header], 
    ["---------------------------"], 
    ["Total Votes: " + str(total_votes)], 
    ["---------------------------"], 
    ["Winner Name: " + winning_person + ": with " + winning_percent + "% and a vote count of " + winning_count], 
    ["2nd Place Name: " + second_person + ": with " + second_percent + "% and a vote count of " + second_count], 
    ["3rd Place Name: " + third_person + ": with " + third_percent + "% and a vote count of " + third_count], 
    ["4th Place Name: " + fourth_person + ": with " + fourth_percent + "% and a vote count of " + fourth_count], 
    ["---------------------------"], 
    ["Winner Name: " + "Congratulations " + winning_person + "!"], 
    ["---------------------------"]
]

for s in txt_lines:
    print(*s)
   
output_path = open("analysis/PyPoll_analysis.txt", "w")
output_path.write(txt_header)
output_path.write("\n") 
output_path.write("---------------------------")
output_path.write("\n") 
output_path.write("Total Votes: " + str(total_votes))
output_path.write("\n") 
output_path.write("---------------------------")
output_path.write("\n") 
output_path.write("Winner Name: " + winning_person + ": with " + winning_percent + "% and a vote count of " + winning_count)
output_path.write("\n") 
output_path.write("2nd Place Name: " + second_person + ": with " + second_percent + "% and a vote count of " + second_count)
output_path.write("\n")  
output_path.write("3rd Place Name: " + third_person + ": with " + third_percent + "% and a vote count of " + third_count)
output_path.write("\n")  
output_path.write("4th Place Name: " + fourth_person + ": with " + fourth_percent + "% and a vote count of " + fourth_count)
output_path.write("\n")  
output_path.write("---------------------------")
output_path.write("\n") 
output_path.write("Winner Name: " + "Congratulations " + winning_person + "!")
output_path.write("\n")  
output_path.write("---------------------------")
output_path.write("\n") 
output_path.close()