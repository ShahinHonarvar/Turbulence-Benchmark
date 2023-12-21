import re
def filter_chars(s):
    return re.sub(r'(?<=\d)B(?!\d)', '', s, flags=re.I)
