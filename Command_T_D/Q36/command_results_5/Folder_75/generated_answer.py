 
import re
def filter_chars(s):
    return re.sub(r'[&;]d|e|f|g|h|i|j|k|l|m', '', s)
