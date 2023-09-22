# import  pandas
#
# data = pandas.read_csv("226 weather_data.csv")
# # # print(type[data])
# # print(type(data['temp']))
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(len(temp_list))
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # # Get data in columns
# # print(data["condition"])
# # print(data.condition)
#
# # # get data in row
# # print(data[data.day == "Monday"])
# # print(data[data.temp==data.temp.max()])
#
# # create a datframe from scratch
#
# data_dict = {
#   "students": ["maxamed", "ali","asma"],
#   "scores": [45, 80, 90]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("228 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count =len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count =len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count =len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
  "fur Color" : ["Gray", "Cinnamon", "Black"],
  "count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

