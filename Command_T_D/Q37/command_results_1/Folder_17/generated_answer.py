 
import re
def filter_chars(s):
    return re.sub(r'[;b]', '', s, flags=re.I)
