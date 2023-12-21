 
import re
def filter_chars(s):
    return re.sub(r'((?:[a-z0-9]{33}[a-z0-9]?.){6}[a-z0-9]{70})', '', s)
