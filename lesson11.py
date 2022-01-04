# json
# csv
import csv

data = []
with open('test.csv', 'r', encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for row in reader:
        data.append(row)

header = data.pop(0)
print(data)
data.append([11, 22, 33])

with open('test_2.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerows(data)

###################################################################
data = []
with open('test.csv', 'r', encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        data.append(row)

for row in data:
    print(row["Total"])


with open('test_3.csv', 'w') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)




#######################################################################
import json

my_data = {"data": [i for i in range(10)], "name": 'John', "age": 23}
print(my_data)
my_data_str = json.dumps(my_data)
print(type(my_data_str), my_data_str)

new_data = json.loads(my_data_str)
print(type(new_data), new_data)

with open("test.json", "w") as json_file:
    json.dump(my_data, json_file, indent=4)

with open("test.json", "r") as json_file:
    data = json.load(json_file)

print(data["data"])