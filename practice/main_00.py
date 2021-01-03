with open('weather_data.csv') as file:
    data = file.readlines()
    # print(data)




import csv

with open('weather_data.csv') as file:
    data = csv.reader(file)
    # print(data)

    temperatures = []
    for row in data:
        # print(row)
        try:
            temperatures.append(int(row[1]))
        except:
            pass

        # or

        if row[1] != 'temp':
            temperatures.append(int(row[1]))
temperatures




import pandas

data = pandas.read_csv('weather_data.csv')
print(data)
print(data['temp'])