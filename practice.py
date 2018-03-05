year = 1789
start = 1
flag=1
with open('stateoftheunion1790-2016.txt','r') as myfile:
    data=myfile.read()

addresses = data.split("***")
date = addresses[229].split('\n')
print (date[4])
stringDate = date[4]
print(stringDate[0:3])
print(stringDate[-4:])

date = addresses[start].split('\n')
stringDate = date[4]
if (stringDate[0:3]=='Jan'):
    monthNumber=1
if (stringDate[0:3]=='Feb'):
    monthNumber=2
if (stringDate[0:3]=='Mar'):
    monthNumber=3
if (stringDate[0:3]=='Apr'):
    monthNumber=4
if (stringDate[0:3]=='May'):
    monthNumber=5
if (stringDate[0:3]=='Jun'):
    monthNumber=6
if (stringDate[0:3]=='Jul'):
    monthNumber=7
if (stringDate[0:3]=='Aug'):
    monthNumber=8
if (stringDate[0:3]=='Sep'):
    monthNumber=9
if (stringDate[0:3]=='Oct'):
    monthNumber=10
if (stringDate[0:3]=='Nov'):
    monthNumber=11
if (stringDate[0:3]=='Dec'):
    monthNumber=12
