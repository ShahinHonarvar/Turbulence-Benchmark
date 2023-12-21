 
import re
def filter_chars(s):
    return re.sub(r"[[\]]|t", "", s, flags=re.I)
