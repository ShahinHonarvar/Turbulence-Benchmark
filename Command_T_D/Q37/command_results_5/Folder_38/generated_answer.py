 
import re
def filter_chars(s):
    return re.sub(r'[a-f]', '', s[24:79])
