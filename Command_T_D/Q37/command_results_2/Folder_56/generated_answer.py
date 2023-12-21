 
import re
def filter_chars(s):
    return re.sub(r'[K-a]', '', s)
