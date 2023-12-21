import re
def filter_chars(s):
    return re.sub(r'(?<=476)b(?!c)d(?=948)', '', s)
