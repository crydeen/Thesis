from __future__ import division
from textstat.textstat import textstat
import nltk
import glob
import re

def lexical_diversity(text):
    return len(set(text)) / len(text)

def word_count(text):
    return len(text)

lexdiv_scores = []
wordcounts = []
grade_levels = []
names = []
wordcounttotal = 0
lexdivtotal = 0
total_grade_level = 0
count = 0


for filename in sorted(glob.glob('Addresses/*.txt')):
    current_last = filename[17:]
    current_last = current_last.replace('.txt','')
    break

for filename in sorted(glob.glob('Addresses/*.txt')):
    new_last = filename[17:]
    new_last = new_last.replace('.txt','')
    if new_last != current_last:
        names.append(current_last)
        current_last = new_last
        avgwordcount = round(wordcounttotal / count, 0)
        avglexdiv = round(lexdivtotal / count, 4)
        wordcounttotal = 0
        lexdivtotal = 0
        count = 0
        lexdiv_scores.append(avglexdiv)
        wordcounts.append(avgwordcount)
    file = open(filename, 'r')
    address = file.read()
    address = address.replace('\n', ' ')
    address = address.replace('  ', ' ')
    address = address.lower()
    address = re.sub(r'\W+', ' ', address)
    address = address.split(" ")
    lexdiv = lexical_diversity(address)
    wordcount = word_count(address)
    wordcounttotal = wordcounttotal + wordcount
    lexdivtotal = lexdivtotal + lexdiv
    count = count + 1
    if filename[10:16] == "201601":
        print("Reaching the end")
        names.append(current_last)
        avgwordcount = round(wordcounttotal / count, 0)
        avglexdiv = round(lexdivtotal / count, 4)
        wordcounttotal = 0
        lexdivtotal = 0
        count = 0
        lexdiv_scores.append(avglexdiv)
        wordcounts.append(avgwordcount)
        break

count = 0

for filename in sorted(glob.glob('Addresses/*.txt')):
    current_last = filename[17:]
    current_last = current_last.replace('.txt','')
    break

for filename in sorted(glob.glob('Addresses/*.txt')):
    new_last = filename[17:]
    new_last = new_last.replace('.txt','')
    if new_last != current_last:
        current_last = new_last
        average_grade_level = round(total_grade_level / count, 3)
        total_grade_level = 0
        count = 0
        grade_levels.append(average_grade_level)
    file = open(filename, 'r')
    address = file.read()
    address = address.replace('\n', ' ')
    address = address.replace('  ', ' ')
    address = address.replace('\r', ' ')
    address = address.replace('  ', ' ')
    address = address.lower()
    grade_level = textstat.flesch_kincaid_grade(address)
    # print(grade_level)
    total_grade_level = total_grade_level + grade_level
    count = count + 1

    if filename[10:16] == "201601":
        current_last = new_last
        average_grade_level = round(total_grade_level / count, 3)
        total_grade_level = 0
        count = 0
        grade_levels.append(average_grade_level)
        break
for index in range(len(lexdiv_scores)):
    print(str(names[index]) + " " + str(wordcounts[index]) + " & " + str(lexdiv_scores[index]) + " & " + str(grade_levels[index]))

# print("Lexical Diversity")
# print(lexdiv_scores)
# print("Word Counts")
# print(wordcounts)
# print("Grade Levels")
# print(grade_levels)
