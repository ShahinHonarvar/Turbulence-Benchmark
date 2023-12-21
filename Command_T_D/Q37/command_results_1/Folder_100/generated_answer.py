import re
def filter_chars(s):
    return re.sub(r'[JQU]88[JQU]90', '', s)
