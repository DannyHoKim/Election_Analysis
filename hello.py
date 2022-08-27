x = 1
while x <= 5:
    print(x)
    x = x + 1

from optparse import Values


counties = ["Fairfax", "Annandale", "Herndon"]

numbers = [0, 1, 2, 3, 4]
for int in numbers:
    print(int)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

print(len(counties))

for i in counties:
    print(i)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voter in counties_dict.items():
    print(f'{county} county has {voter} registered voters.')
for i in counties_dict:
    print(i)

for i in counties_dict.keys():
    print(i)

for i in counties_dict.values():
    print(i)

for county, voters in counties_dict.items():
    print(str(county) + "county has" + str(voters) + "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for x in county_dict.values():
        print(x)


for counties_dict in voting_data:
    print(counties_dict['registered_voters'])

# multiline f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    # f"You received {candidate_votes / total_votes * 100}% of the total votes.")
# format floating-point decimals
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)


# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")