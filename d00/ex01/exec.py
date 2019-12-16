import sys

if __name__ == "__main__":
    result = []
    for index, arg in enumerate(sys.argv):
        if index == 0:
            continue
        'Reverse string'
        arg = "".join(reversed(arg))
        'Change the case of string'
        string = ""
        for letter in arg:
            if letter.islower():
                string += letter.upper()
            elif letter.isupper():
                string += letter.lower()
            else:
                string += letter
        'put strings together'
        result.append(string)
    result.reverse()
    if (len(result) > 0):
        print(" ".join(result))
