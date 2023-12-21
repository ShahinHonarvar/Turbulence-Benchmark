import re
def filter_chars(s):
    return re.sub(r'((?<=[b-e])h-j)', '', s)
