 
import re
def filter_chars(str):
    return re.sub(r'[A-Q][^A-Q]*', '', str)
