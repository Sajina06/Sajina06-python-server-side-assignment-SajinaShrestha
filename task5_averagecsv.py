import csv 
total=0
count=0

with open('marks.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Marks']:
            marks = int(row['Marks'])
        total+=marks
        count+=1
    if count > 0:
        avg = total / count
        print(f"average marks :{avg}")
    else:
        print("no data")