 
import re
def filter_chars(s):
    return re.sub(r'[^A-Z]{669,888}', '', s)
