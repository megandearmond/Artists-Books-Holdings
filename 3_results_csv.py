import csv
import json
# import itertools

everything_tabled = []
with open('everything.txt', 'r') as in_file:

 
    AB_data = json.load(in_file)

   
    with open('everything.csv', 'w') as out_file:
        AB_forCSV = csv.writer(out_file)

        for a_row in AB_data:
            AB_forCSV.writerow([a_row["t"],a_row["a"],a_row["holding_number"],a_row["oclc_number"]])

  