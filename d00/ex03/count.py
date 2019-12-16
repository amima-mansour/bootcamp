import re


def text_analyzer(param=""):
    ''' displays the sums of upper characters, lower characters,
        punctuation characters and spaces in a given text.
    '''
    while len(param) == 0:
        param = input('What is the text to analyse?\n')
    print("The text contains {} characters:".format(len(param)))
    count = len(re.findall("[A-Z]", param))
    print('- {} upper letters'.format(count))
    count = len(re.findall("[a-z]", param))
    print('- {} lower letters'.format(count))
    count = len(re.findall("[\'.,;:-]", param))
    count += param.count('\"')
    count += param.count('!')
    count += param.count('?')
    count += param.count(')')
    count += param.count('(')
    count += param.count('[')
    count += param.count(']')
    print('- {} punctuation marks'.format(count))
    count = len(param.split())
    if count > 0:
        count -= 1
    print("- {} spaces".format(count))
