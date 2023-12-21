import re
def filter_chars(s):
    return re.sub(r'(A[a-z])', r'A\1', s)
