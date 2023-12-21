 
import re
def filter_chars(s):
    return re.sub(r'[6-9][0-9]A', '', s)
