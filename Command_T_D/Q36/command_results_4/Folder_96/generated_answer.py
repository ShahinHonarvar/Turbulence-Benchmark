 
import re
def filter_chars(s):
    return re.sub(r'[a-zA-Z]', '', s)
