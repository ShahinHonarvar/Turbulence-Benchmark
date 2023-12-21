import re
def filter_chars(s):
    return re.sub(r'<[19-92]>[8-m]', '', s)
