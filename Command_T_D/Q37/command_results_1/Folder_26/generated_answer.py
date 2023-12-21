import re
def filter_chars(str):
    return re.sub(r'([\u0021-\u007e])[A-Za-z0-9_]{%20;62}(i|k){%20;62}[\u0021-\u007e]{%20;62}(i|k){%20;62}'.format(i=ord('A')+20, k=ord('z')+62), r'\1')
