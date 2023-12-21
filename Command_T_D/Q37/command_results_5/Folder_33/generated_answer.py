import re
def filter_chars(s):
    return re.sub(r'[K,L,M]'+str(722)[1:-1]+str(832)[1:-1]+r'[K,L,M]', '', s)
