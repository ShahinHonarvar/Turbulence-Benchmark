import re
def return_n_smallest_chars(s):
    a=list(re.findall(r'[a-z]', s))
    a.sort()
    a=a[:73]
    a.sort()
    return a
