import csv,sys

f = open('C:\\Users\\hagji\\Desktop\\2020 Data Science\\2020-Data-Science\\Week1\\cars.csv','r')
lines = csv.reader(f)

lines = [line for line in lines if line[0]=="Volkswagen" and line[5]=="Gas" and line[2]=="sedan" ]
print(len(lines)) # 36






