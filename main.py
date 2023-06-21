# # with open("weather_data.csv",mode="r") as weather_file:
# #     data = weather_file.read().split("\n")

# # import csv

# # with open("weather_data.csv") as weather_file:
# #     data = csv.reader(weather_file)
# #     tempratures=[]
# #     count=0
# #     for row in data:
# #         if count==0:
# #             pass
# #         else:
# #             tempratures.append(int(row[1]))
# #         count+=1

# # print(tempratures)

# import pandas 

# weather_data = pandas.read_csv("weather_data.csv")
# # print(weather_data)
# # print(weather_data["temp"])

# ## Convert data frame to dictionary
# # data_dic = weather_data.to_dict()
# # print(data_dic)

# # Convert series (datarow or data column) to list 
# temp_list = weather_data["temp"].to_list()
# ## Calculate the average temp

# # Old school way below
# # mean_temp = sum(temp_list)/len(temp_list)
# # print(round(mean_temp,2))

# # By Pandas lib
# mean_temp = weather_data["temp"].mean()
# print(mean_temp)
# max_temp = weather_data["temp"].max()
# print(max_temp)
# # Get the row which has max temp
# max_temp_row = weather_data[ weather_data["temp"] == max_temp ]
# print(max_temp_row)
# # Create Data Frame
# my_dic = { 
#     "students" : ["Amy", "James", "Lily"],
#     "grades" : [75, 65, 100]
# }

# students_data = pandas.DataFrame(my_dic)
# print(students_data)
# ## Create Csv file into file path
# students_data.to_csv("students_data.csv")

#### BIG DATA Challenge

import pandas

main_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
number_of_gray = len(main_data[ main_data["Primary Fur Color"] == "Gray" ])
number_of_cinnamon = len(main_data[ main_data["Primary Fur Color"] == "Cinnamon"])
number_of_black = len(main_data[main_data["Primary Fur Color"] == "Black"])
color_types = {
    "Fur Color" : ["gray","red","black"],
    "Count" : [number_of_gray, number_of_cinnamon, number_of_black]
}
color_types_frame = pandas.DataFrame(color_types)
color_types_frame.to_csv("squirrel_types_count.csv")