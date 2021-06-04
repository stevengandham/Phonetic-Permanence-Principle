import json

arpabet_dictionary = dict()

# to create our arpabet table
# read each line, split by \t and append to dictionary
with open("cmudict_SPHINX_40.txt", 'r') as file:
    line = file.readline()
    while line != '':
        [key, val] = line.replace('\n', '').split("\t", 1)
        # print(key)
        # print(val)
        arpabet_dictionary[key] = val
        line = file.readline()
        # break;

# convert to json file
with open("arpabetTable.json", 'w') as writeTo:
    json.dump(arpabet_dictionary, writeTo)
