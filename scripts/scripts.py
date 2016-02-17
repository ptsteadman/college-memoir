import nltk
sentence = """Amethyst Amelia Kelly, better known by her stage name Iggy Azalea, has announced plans to spend an entire week in a KFC eating fried chicken wings after being dumped by her
manager, rapper and music mogul T.I., because she 'needs time to think'."""
tokens = nltk.word_tokenize(sentence)
print tokens
tagged = nltk.pos_tag(tokens)
print tagged
