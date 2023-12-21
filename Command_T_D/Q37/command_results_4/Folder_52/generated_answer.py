 
import re
def filter_chars(text):
    return re.sub(r'(?i)([jve])', r'\\1', text)
