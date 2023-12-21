 
import re
def filter_chars(s):
    return re.sub(r'[Rr]e[ft]t', '', s)
