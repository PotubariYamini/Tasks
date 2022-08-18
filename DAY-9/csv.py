import csv # importing csv
with open("salary.csv",mode='r')as csv_file: # opening file with open

    
    csvreader= csv.reader(csv_file,delimiter=',')
    for line in csvreader:
        print(line)
