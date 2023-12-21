import re
def remove_repeat_chars(s):
    return re.sub(r'(?<=43)\w+\w+\w+\w+(?<=70)', '', s)
