import re
def return_n_smallest_chars(s):
    small = sorted(set(re.findall(r'[a-z]', s)), key=lambda x: ord(x))[:84]
    return small
