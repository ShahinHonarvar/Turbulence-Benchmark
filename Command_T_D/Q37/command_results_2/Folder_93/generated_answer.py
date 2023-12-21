import re
def filter_chars(s):
    return re.sub(r'(?!\A)[38-69]H[38-69]e\Z', '', s)
