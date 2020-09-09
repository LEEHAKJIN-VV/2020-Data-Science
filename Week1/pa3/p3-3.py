import csv,sys
f = open('C:\\Users\\hagji\\Desktop\\2020 Data Science\\2020-Data-Science\\Week1\\cars.csv','r')

head = list(f.readline().rstrip().split(','))
lines = csv.reader(f)

car_dict={}
car_list=[]

for line in lines:
    for i in range(0,len(head)):
        car_dict[head[i]] = line[i]

    car_list.append(car_dict.copy())

car_set=set()

for car in car_list:
    car_set.add(car['Brand'])

print(car_set)