import re
def filter_chars(s):
    return re.sub(r'<(b|e|g|i|j|l|o|t)', '', s)
