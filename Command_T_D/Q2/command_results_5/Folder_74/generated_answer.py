import re
def all_ints_exclusive(x):
    y = re.findall(r'[0-9]', x)
    return list(set(y) - set('0123456789'))
