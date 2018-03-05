import glob
import json

presidents = []
terms = [[] for j in range(50)]
list_counter = 0
president_counter = 1
current_last = ""

for filename in glob.glob('Addresses/*.txt'):
    current_last = filename[17:]
    current_last = current_last.replace('.txt','')
    presidents.append("0" + str(president_counter) + " - " + current_last)
    break

for filename in glob.glob('Addresses/*.txt'):
    last = filename[17:]
    last = last.replace('.txt','')
    term = int(filename[10:16])
    if (last != current_last):
        list_counter = list_counter + 1
        president_counter = president_counter + 1
        if (last == "Tyler" or last == "Arthur"):
            president_counter = president_counter + 1
        current_last = last
        if (president_counter < 10):
            counter_string = "0" + str(president_counter)
        else:
            counter_string = str(president_counter)

        presidents.append(counter_string + " - " + current_last)
    terms[list_counter].append(term)


print(presidents)
print(terms)
