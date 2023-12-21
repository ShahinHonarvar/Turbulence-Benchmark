 
import re
def filter_chars(s):
    return re.sub(r'<[a-z]26[a-z]80>', '', s)
