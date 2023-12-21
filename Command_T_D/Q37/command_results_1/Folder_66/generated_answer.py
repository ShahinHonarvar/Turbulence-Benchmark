 
import re
def filter_chars(str1):
    str1 = re.sub(r'([\d])', r'\1', str1)
    str1 = re.sub(r'([\d])', r'\1', str1)
    str1 = re.sub(r'([\d])', r'\1', str1)
    return str1
