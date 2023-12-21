 
import re
def filter_chars(s):
    return re.sub(r'[A-i]+', '', s)
