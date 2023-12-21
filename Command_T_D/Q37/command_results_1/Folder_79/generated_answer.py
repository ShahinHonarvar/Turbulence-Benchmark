 
import re
def filter_chars(s):
    return re.sub(r'([@T])', '', s, flags=re.I)
