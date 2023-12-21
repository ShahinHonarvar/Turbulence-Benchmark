 
import re
def filter_chars(s):
    return re.sub(r'(?!f)[a-z]{%d}|{%d}(?!%|)', '', s)
