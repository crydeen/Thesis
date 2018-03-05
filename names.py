import glob

presidents = []
terms = [[] for j in range(50)]
list_counter = 0
current_last = ""

for filename in glob.glob('Addresses/*.txt'):
    current_last = filename[17:]
    current_last = current_last.replace('.txt','')
    presidents.append(current_last)
    break

for filename in glob.glob('Addresses/*.txt'):
    last = filename[17:]
    last = last.replace('.txt','')
    term = int(filename[10:16])
    if (last != current_last):
        list_counter = list_counter + 1
        current_last = last
        presidents.append(current_last)
    terms[list_counter].append(term)


print(presidents)
print(terms)
