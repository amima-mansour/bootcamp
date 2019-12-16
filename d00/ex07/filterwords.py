import sys
import re


try:
    assert len(sys.argv) == 3
    assert not sys.argv[1].isdigit()
    n = int(sys.argv[2])
    words = re.sub(r'[^\w\s]', '', sys.argv[1])
    words = words.split(" ")
    filteredwords = filter(lambda x: len(x) > n, words)
    print(list(filteredwords))
except (ValueError, AssertionError):
    print("ERROR")
