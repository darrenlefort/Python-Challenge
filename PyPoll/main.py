import csv
import os

pathway = os.path.join("..", "PyPoll_data.csv")

with open (pathway) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile, None)
    print(f"Header: {csv_header}")