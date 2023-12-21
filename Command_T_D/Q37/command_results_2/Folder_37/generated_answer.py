import re
def filter_chars(s):
    return re.sub(r'[A-O][A-Z][A-^Z]','',s)
