import glob
import re

for filename in glob.glob('Addresses/*.txt'):
    file = open(filename, 'r')
    address = file.read()
    address = address.replace('\n', ' ')
    address = address.replace('  ', ' ')
    address = address.lower()
    address = re.sub(r'\W+', ' ', address)
    address = address.split(" ")
    print("NEW SPEECH")
    print(address)
    print("END SPEECH")
