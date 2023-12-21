 
import re
def filter_chars(s):
    return re.sub(r'[g-~]', '', s, flags=re.I)
