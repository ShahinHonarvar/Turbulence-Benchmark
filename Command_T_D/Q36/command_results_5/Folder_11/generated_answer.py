 
import re
def filter_chars(s):
    return re.sub(r'[A-Z][^A-Z]86[A-Z][^A-Z]93', '', s)
