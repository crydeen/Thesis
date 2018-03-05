import operator
import re
import json
import glob

# addresses = re.sub('@"(?<!\n)\n"', ' ', addresses)
for filename in glob.glob('Addresses/*.txt'):
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

    ct_dct={}
    int_dct={}
    array_dct = []
    for word in address:
        if not word in common:
            try:
                ct_dct[word]=ct_dct[word]+1
            except:
                ct_dct[word]=1

    del ct_dct[""]

    for key,value in ct_dct.iteritems():
        int_dct = {}
        int_dct['text'] = key
        int_dct['size'] = value
        array_dct.append(int_dct)

    last = filename[10:]
    last = last.replace('.txt','')
    last = 'web/thesis/JSON/' + last + '.json'

    with open(last, 'w') as fp:
        json.dump(array_dct, fp)
