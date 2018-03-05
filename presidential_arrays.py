import operator
import re
import json
import glob

pres_counter = 0;
ct_dct={}
int_dct={}
array_dct = []

for filename in glob.glob('Addresses/*.txt'):
    current_last = filename[17:]
    current_last = current_last.replace('.txt','')
    break

for filename in glob.glob('Addresses/*.txt'):
    last = filename[17:]
    last = last.replace('.txt','')
    if (last != current_last):
        del ct_dct[""]
        int_dct={}
        array_dct = []
        for key,value in ct_dct.iteritems():
            int_dct = {}
            int_dct['text'] = key
            int_dct['size'] = value
            array_dct.append(int_dct)
        number = ''
        if pres_counter < 10:
            number = '0' + str(pres_counter)
        else:
            number = str(pres_counter)
        new_file = 'web/thesis/JSON/' + number + current_last + '.json'
        with open(new_file, 'w') as fp:
            json.dump(array_dct, fp)
        current_last = last
        ct_dct={}
        pres_counter = pres_counter + 1

    file = open(filename, 'r')
    address = file.read()
    address = address.replace('\n', ' ')
    address = address.replace('  ', ' ')
    address = address.lower()
    address = re.sub(r'\W+', ' ', address)
    address = address.split(" ")

    common = open("common.txt", "r")
    common=common.read()
    common=common.lower()
    common=common.split("\n")


    for word in address:
        if not word in common:
            try:
                ct_dct[word]=ct_dct[word]+1
            except:
                ct_dct[word]=1

int_dct={}
array_dct = []
del ct_dct[""]
for key,value in ct_dct.iteritems():
    int_dct = {}
    int_dct['text'] = key
    int_dct['size'] = value
    array_dct.append(int_dct)
number = str(pres_counter)
new_file = 'web/thesis/JSON/' + number + current_last + '.json'
with open(new_file, 'w') as fp:
    json.dump(array_dct, fp)
