 
import re
def filter_chars(s):
    return re.sub(r'([\d])([a-e]{2})', r'\1', s)
