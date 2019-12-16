import random

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''

    try:
        assert isinstance(text, str)
        text_list = text.split(sep)
        if option is None:
            return text_list
        else:
            assert option in ['shuffle', 'unique', 'ordered']
            if option == 'suffle':
                random.shuffle(text_list)
                return text_list
            elif option == 'unique':
                return list(set(text_list))
            else:
                return text_list.sort()

    except AssertionError:
        print("ERROR GENERATOR")
