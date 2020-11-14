import csv

list= []

def readcsv():
    listtest = []
    with open('1.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         listtest.append(row)
     return listtest;

list = readcsv()

for x in list:
    print(x)



#Musterlösung
#import csv
#with open('departments.csv', newline='') as csvfile:
#    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in data:
#        print(', '.join(row))