# with open("weather_data.csv", "r") as data:
#     data = data.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = list(csv.reader(data_file))
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")  # this stores the csv data into a pandas dataframe object
# print(type(data))
# print(data["temp"])

# # storing the temperature in a list
# # temp_list = data["temp"].to_list()
# # print(temp_list)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# # calculate the average temperature. This requires adding all values and dividing it by the total number of
# # values (in this case the length of the list)
#
# # Step 1: calculate the sum of temperatures
# calc_temp = 0
# for values in data_dict['temp']:
#     calc_temp += data_dict['temp'][values]
#
# # Step 2: calculate average of the temperatures using the length function
# average = calc_temp / len(data_dict['temp'])
# print(f'The average temperature is {int(average)}.')
#
# print(f"The max temperature is {data['temp'].max()}")
# print(data['temp'].mean())

# Get data in a specific row
# print(data[data.temp == data.temp.max()])

# Get Monday temperature in C and convert to F

# Step 1: get temperature from pandas dataframe
monday = data[data.day == 'Monday']
monday_temp = monday.temp

# Step 2: Convert temperature from C to F
# C to F formula: multiply by 9/5 and add 32

F = (monday_temp * (9 / 5)) + 32
print(F)

# How to create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)