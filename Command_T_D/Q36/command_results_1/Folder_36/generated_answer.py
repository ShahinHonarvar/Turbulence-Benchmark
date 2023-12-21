 
import re
def filter_chars(s):
    return re.sub(r'(?i)[A-Z][\d][A-Z][\d]>[ll<]', '', s)
