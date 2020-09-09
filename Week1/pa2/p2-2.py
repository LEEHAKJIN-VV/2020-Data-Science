import csv,sys

f = open('C:\\Users\\hagji\\Desktop\\2020 Data Science\\2020-Data-Science\\Week1\\cars.csv','r')
lines = csv.reader(f)

lines = [line for line in lines if line[0] =="BMW"]
lines.sort(key=lambda x: x[7])

print(len(lines)) # 694

for line in lines:
    sys.stdout.write(str(line) + '\n')