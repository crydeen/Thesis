import json

sample = {'words':1629, 'testing':1233, 'hello':1000}

with open('result.json', 'w') as fp:
    json.dump(sample, fp)
