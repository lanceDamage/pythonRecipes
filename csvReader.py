'''
In this py3 recipe, I'll import some simple data from local location within the spyder file
'''
#first, I'll import some important tools
import csv
#this will format the csvcar
Reader = csv.reader(open('mycardata.csv',newline=''),delimiter=' ')
#now I will iterate through the csv
for row in carReader:
    print(', '.join(row))
