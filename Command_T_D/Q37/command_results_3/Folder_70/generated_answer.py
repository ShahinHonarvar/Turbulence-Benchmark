import re
def filter_chars(str):
    return re.sub(r'[A-Z]+', '', str[515:-1])
