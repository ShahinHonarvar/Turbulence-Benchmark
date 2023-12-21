import re
def filter_chars(str):
    return re.sub(r'([Rr][^t]*)', '', str)
