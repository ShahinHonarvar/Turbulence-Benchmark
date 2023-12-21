 
import re
def filter_chars(s):
    return re.sub(r'I|J|K', '', s[10:69])
