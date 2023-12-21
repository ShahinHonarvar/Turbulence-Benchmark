import re
def filter_chars(s):
    return re.sub(r'([9-s]){125}([9-s]){855}', '', s)
