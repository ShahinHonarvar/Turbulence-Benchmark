 
import re
def filter_chars(s):
    return re.sub(r'[Qh]', '', s, flags=re.I)
