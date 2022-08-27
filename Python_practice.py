# # print("hello world")
# # Types of Data
# # Integers,Floats, String, Boolean
# a = 4
# b = 3.33
# c = "Three"
# d = True 
# print(type(a))

# # Declaring Variable (Use variable names that help make data clear (name = "Danny")
# num_candidates = 3
# winning_percentage = 73.81
# candidate = "Diane"
# won_election = True
# print(candidate)

# #keywords cannot be used as variable names
#     # help("keywords")

# #arithmetic operators
#     # x+y
#     # x-y
#     # x*y
#     # x/y
#     # x%y % is the modulus it will divide then return the remainder
#     # x//y divides one number by another and returns Integer
#     # x**y x to the power of y

# #lists
# Cities = ["San Diego", "Fairfax", "Eastlake"]
# print(Cities)
# print(Cities[0])
# print(Cities[-2])
# print(len(Cities))
# Cities.append("Chula Vista")
# print(Cities)
# print(Cities[0:2])
# Cities.pop(1)
# print(Cities)

#Dictionaries
# countries_dict = {
#     'Arapahoe': 422829,
#     'Denver': 463353,
#     'Jefferson': 432438
# }
# print (f"{countries_dict['Arapahoe']} is the number of voters in Arapahoe")

# print(len(countries_dict))
# print(countries_dict)
# print(countries_dict['Denver'])

#lists of Dictionaries
# voting_data = [
#     {"county":"Arapahoe", "registered_voters": 422829},
#     {"county":"Denver", "registered_voters": 463353},
#     {"county":"Jefferson", "registered_voters": 432438}
# ]

# print(voting_data)
# print(voting_data[0]), print(voting_data[1])
# print(len(voting_data))

# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[2] == "Denver":
#     print(counties[2])

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")


# #What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')


# # What is the score?
# score = int(input("What is your test score? "))

# # Easier to read
# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

