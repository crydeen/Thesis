import nltk
f = open('179001_Washington.txt')
raw = f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
