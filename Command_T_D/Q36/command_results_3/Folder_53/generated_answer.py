import re
def filter_chars(str1):
    return re.sub(r'[A-Z][^A-Z]90[A-Z][^A-Z]97', '', str1)
