import re
def filter_chars(s):
    return re.sub(r'([\u17e0-\u17ef]+)', '', s)
