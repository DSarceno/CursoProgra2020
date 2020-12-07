#   This script needs two arguments in terminal after the python command:
#       - 0: attendande.py
#       - 1: csv file with previous assistance
#       - 2: txt file with assistance list

import sys

attendance_file = sys.argv[2]
dataBase = sys.argv[1]

data_base_file = open(dataBase, "r")

data_base = []
for line in data_base_file:
    data_base.append(line.split(","))

fo = open(attendance_file, "r")
attendance_list = fo.readlines()

# Add to a column attendande
data_base[0][-1] = data_base[0][-1][0]
data_base[0].append('1\n')

for assitent in attendance_list:
    for person in data_base:
        if assitent[:-1] == person[0]:
            person[-1] = person[-1][0]
            person.append('1\n')
            entries = len(person)
            continue

for person in data_base:
    if len(person) < entries:
        person[-1] = person[-1][0]
        person.append('0\n')

fo.close()
data_base_file.close()

# Write the new csv file
new_data_base = open("data_base.csv", "w")
for elem in data_base:
    for word in elem:
        if elem[-1] == word:
            new_data_base.write(str(word))
        else:
            new_data_base.write(str(word)+",")

new_data_base.close()
