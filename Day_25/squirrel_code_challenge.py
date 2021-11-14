import pandas
import pandas as pd
import numpy as np

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_colour_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_colour_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_colour_count = len(data[data["Primary Fur Color"] == "Black"])

fur_colour_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
                   "Count": [gray_colour_count, cinnamon_colour_count,black_colour_count]
                   }

new_dframe = pandas.DataFrame(fur_colour_dict)

new_dframe.to_csv("fur_colour.csv")

# print(color_count)
# print(type(color_count))
# # fur_color.pd.DataFrame.to_dict()
# print(color_count[2])

# print(color_count)

# df = pd.DataFrame(columns=['Colour', 'Count'], data=color_count)
# print(color_count)
