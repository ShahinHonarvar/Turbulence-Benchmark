import re
def filter_chars(strng):
    return re.sub(r'[EIOU]l', '', strng)
