import csv
import os

os.makedirs("output", exist_ok=True)

input_file = "input/data.csv"
output_file = "output/processed.csv"

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	for row in reader:
		if row:
			writer.writerow(row)

print("File processed")