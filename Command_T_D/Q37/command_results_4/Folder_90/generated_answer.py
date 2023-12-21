 
import re
def filter_chars(s):
    return re.sub(r'[a-j][\d]b', '', s)
