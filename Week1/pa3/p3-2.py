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

sort_car_list = [car for car in car_list if car['Price']!='NA' and 20000 <= int(float(car['Price'])) <= 50000 and int(car['Year']) >= 2000 and car['Body']=="sedan"]
sort_car_list.sort(key=lambda car: car['Price'])

len(sort_car_list) # 292
for car in sort_car_list:
    print(car)