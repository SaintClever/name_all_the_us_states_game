import pandas

data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data)
# print(data['temp'])

data_dict = data.to_dict()
# print(data_dict)
# print('')

temp_list = data['temp'].to_list()
# print(temp_list)
# print(len(temp_list))


# Average temp
total = 0
for deg in temp_list:
    total += deg
average = total / len(temp_list)
print('{:.2f}'.format(average))


# or
average = sum(temp_list) / len(temp_list)
print('{:.2f}'.format(average))


# or with pandas
average = data['temp'].mean()
print('{:.2f}'.format(average))


# Max temp with pandas
max_num = data['temp'].max()
print(max_num)
print('')


# print(data['condition'])
# print('')

# print(data.condition)


'''To get columns in pandas'''
monday_column = data[data.day == 'Monday']
print(monday_column)
print('')

max_column = data[data['temp'] == data['temp'].max()]
print(max_column)
print('')

monday = data[data['day'] == 'Monday']
print(monday['condition'])
monday_celsius = monday['temp']

monday_temp = (monday_celsius * 9/5) + 32
print(monday_temp)
print('')

'''Create a dataframe from scratch'''
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

df = pandas.DataFrame(data_dict)
print(df)


df.to_csv('new_data.csv')

