import re
def filter_chars(s):
    return re.sub(r'(9|8|7|6|5|4|3|2|1)', '', s)
