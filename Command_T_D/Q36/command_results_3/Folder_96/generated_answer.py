import re
def filter_chars(s):
    return re.sub(r'([\d\w])([\d\w]38[\d\w]81[\d\w])([\d\w])', r'\1.\2.\3', s)
