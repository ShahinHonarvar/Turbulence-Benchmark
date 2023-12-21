import re
def filter_chars(str1):
    return re.sub(r'<([^w]*)>([^<]*)<w>([^>]*)(>)', r'\2', str1)
