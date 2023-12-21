import re
def filter_chars(s):
    return re.sub(r'(?<=.)(6[a-w])', '', s)
