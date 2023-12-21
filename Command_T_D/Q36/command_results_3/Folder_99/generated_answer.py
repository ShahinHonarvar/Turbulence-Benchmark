 
import re
def filter_chars(s):
    return re.sub(r'([^b]d)', '', s, flags=re.I)
