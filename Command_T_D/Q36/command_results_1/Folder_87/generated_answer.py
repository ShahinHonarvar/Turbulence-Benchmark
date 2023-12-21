import re
def filter_chars(str):
    return re.sub(r'(3[a-d]*)', r'\1', str)
