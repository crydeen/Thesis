start = 1
flag=1
with open('stateoftheunion1790-2016.txt','r') as myfile:
    data=myfile.read()

addresses = data.split("***")
file = open('index.txt','w')
file.write(addresses[0])

while (flag == 1) :
    info = addresses[start].split('\n')
    stringDate = info[4]
    year = stringDate[-4:]

    name = info[3].split(' ')
    if (len(name) == 2 or name[1] == 'Obama'):
        lastname= name[1]
    if (len(name) == 3 and name[1] != 'Obama'):
        lastname = name[2]

    if (stringDate[0:3]=='Jan'):
        monthNumber = '01'
    if (stringDate[0:3]=='Feb'):
        monthNumber = '02'
    if (stringDate[0:3]=='Mar'):
        monthNumber = '03'
    if (stringDate[0:3]=='Apr'):
        monthNumber = '04'
    if (stringDate[0:3]=='May'):
        monthNumber = '05'
    if (stringDate[0:3]=='Jun'):
        monthNumber = '06'
    if (stringDate[0:3]=='Jul'):
        monthNumber = '07'
    if (stringDate[0:3]=='Aug'):
        monthNumber = '08'
    if (stringDate[0:3]=='Sep'):
        monthNumber = '09'
    if (stringDate[0:3]=='Oct'):
        monthNumber = '10'
    if (stringDate[0:3]=='Nov'):
        monthNumber = '11'
    if (stringDate[0:3]=='Dec'):
        monthNumber = '12'

    filename= str(year)+monthNumber+'_'+lastname+".txt"
    file=open(filename,"w")
    file.write(addresses[start])
    start += 1

    if (year == '2016'):
        flag = 0;
