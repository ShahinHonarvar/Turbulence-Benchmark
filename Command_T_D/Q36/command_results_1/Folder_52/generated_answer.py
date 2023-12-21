 
import re
def filter_chars(s):
    return re.sub(r'(?<![a-z]){49,56}(?=[a-z])', '', s)
