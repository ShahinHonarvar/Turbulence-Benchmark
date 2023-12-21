 
import re
def filter_chars(s):
    return re.sub(r'[A-Z][^v]{%379,%898}', '', s)
