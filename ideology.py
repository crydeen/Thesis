from __future__ import division
import numpy as np
import glob
import re

lexicon = open("lex.csv","r")
lexicon = lexicon.read()
lexicon = lexicon.split("\r\n")
for index in range(len(lexicon)):
    lexicon[index]=lexicon[index].split(",")
    try:
        lexicon[index][1] = np.float32(lexicon[index][1])
    except:
        del(lexicon[index])

ideology_score={}
ideology = {}

for filename in glob.glob('Addresses/*.txt'):
    file = open(filename, 'r')
    address = file.read()
    address = address.replace('\n', ' ')
    address = address.replace('  ', ' ')
    address = address.lower()
    address = re.sub(r'\W+', ' ', address)
    address = address.split(" ")

    ct_dct={}
    for word in address:
        try:
            ct_dct[word]=ct_dct[word]+1
        except:
            ct_dct[word]=1

    score_array=[]
    for key, value in ct_dct.items():
        for index in range(len(lexicon)):
            if key == lexicon[index][0]:
                score_array.append([lexicon[index][1], value])
                break

    for index in range(len(score_array)):
        product = score_array[index][0] * score_array[index][1]
        try:
            total = total + product
            count = count + score_array[index][1]
        except:
            total = product
            count = score_array[index][1]

    final_score = total/count
    ideology_score[filename] = final_score

for title in glob.glob('Addresses/*.txt'):
    if (ideology_score[title] <= -0.02 and ideology_score[title] >=-1.00):
        ideology[title] = "Liberal"
    elif (ideology_score[title] > -.02 and ideology_score[title] < .02):
        ideology[title] = "Moderate"
    elif (ideology_score[title] >=.02 and ideology_score[title] <= 1.00):
        ideology[title] = "Conservative"
    else:
        ideology[title] = "error"

for key, value in ideology.items():
    print(key + " --> " + value)
