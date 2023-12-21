import re
def filter_chars(s):
    return re.sub(r'(?<=f)[:{]85[:{]89', '', s)
