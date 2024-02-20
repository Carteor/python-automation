import csv

merges = []

with open('input.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        merges.append({'merged_column':row['Company Name']+' '+row['Website']})

with open('output.csv', mode='w') as output_file:
    fieldnames = ['merged_column']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    for merge in merges:
        writer.writerow(merge)