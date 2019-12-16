phrase = "The right format"
length = 42 - len(phrase) - 1
print('{}{}'.format(chr(45) * length, phrase))
