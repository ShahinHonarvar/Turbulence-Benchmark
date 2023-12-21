import re
def filter_chars(s):
    return re.sub(r'<[A-Z][A-Z]B[A-Z]C', '', s)
