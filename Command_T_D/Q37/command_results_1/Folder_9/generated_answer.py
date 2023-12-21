import re
def filter_chars(s):
    return re.sub(r'(A[38-99])', r' \1', s)
