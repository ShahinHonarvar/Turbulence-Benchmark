 
import re
def filter_chars(s):
    return re.sub(r'[!x]', '', s, flags=re.I)
