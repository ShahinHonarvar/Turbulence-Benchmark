import re
def filter_chars(strng):
    return re.sub(r'<[A-Z]{1,6}>.*?<[A-Z]{1,6}', '', strng)
