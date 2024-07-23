import csv

with open('myfile.csv', 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        print(line)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
with open('myfile.csv', 'r') as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:
        print(line)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
rows = []
with open('myfile.csv', 'r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)
    for line in csvFile:
        rows.append(line)
print(rows)
for row in rows:
    print(row)