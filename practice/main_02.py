import pandas as pd


data = pd.read_csv('2018_central_park_squirrel_census_data.csv')
# print(data.count())

fur_colors = data['Primary Fur Color']
# print(fur_colors)


# data['Black' == data['Primary Fur Color']].count().max()


colors = []
for color in fur_colors:
    if color not in colors and type(color) == str:
        colors.append(color)
# print(colors)


count = []
for color in colors:
    # count.append(data[color == data['Primary Fur Color']].count().max())

    # or
    count.append(len(data[color == data['Primary Fur Color']]))
# print(count)


data = {'Fur Color': colors, 'Count':count}
df = pd.DataFrame(data)
print(df)

# Turn df to csv
df.to_csv('squirrel_census_color_data_2018.csv')
