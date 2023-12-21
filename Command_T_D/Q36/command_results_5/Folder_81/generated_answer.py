 
import re
def filter_chars(s):
    return re.sub(r'([A-Z])([0-9])([A-Z])', r'\2\1\3', s)
