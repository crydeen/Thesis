import operator
import re
import csv

addresses = open('stateoftheunion1790-2016.txt','r').read()

# addresses = re.sub('@"(?<!\n)\n"', ' ', addresses)

addresses = addresses.replace('\n', ' ')
addresses = addresses.replace('  ', ' ')
addresses = addresses.lower()
addresses = re.sub(r'\W+', ' ', addresses)
addresses = addresses.split(" ")

common = open("common.txt", "r")
common=common.read()
common=common.lower()
common=common.split("\n")

ct_dct={}
for word in addresses:
    if not word in common:
        try:
            ct_dct[word]=ct_dct[word]+1
        except:
            ct_dct[word]=1

deleteArray = []
for key, value in ct_dct.items():
    if value < 250:
        deleteArray.append(key)

for word in deleteArray:
    del ct_dct[word]

sorted_dict = sorted(ct_dct.items(), key=operator.itemgetter(1))

# writing to a csv - https://docs.python.org/3/library/csv.html
with open('dict.csv', 'wb') as csvfile:
    for key, value in sorted_dict:
        print(key + " --> " + str(value))
        dictwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        dictwriter.writerow([key])
