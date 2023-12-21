 
import re
def filter_chars(str1):
    return re.sub(r'([A-Z][a-z]*)W([A-Z][a-z]*)y', r'\1X\2', str1)
