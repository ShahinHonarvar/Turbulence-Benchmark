import re
def filter_chars(str):
    for c in range(171, 636):
        for i in range(len(str)):
            if str[i] == chr(c):
                str = re.sub(chr(c), '', str)
    return str
