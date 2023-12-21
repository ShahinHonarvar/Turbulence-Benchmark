import re
def filter_chars(s):
    return re.sub(r'[Vv]?' + '[:;]'.join(map(str, list(range(69, 97)))), '', s)
