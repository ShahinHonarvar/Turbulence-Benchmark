 
import re
def filter_chars(s):
    return re.sub(r'(?<=.)(W[a-z]){0,62}(?:[A-Z] |[a-z])', '', s)
