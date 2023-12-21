import re
def filter_chars(s):
    return re.sub(r'[^a-z0-9]{%19,%33}(?<=s{%19,%33})[^a-z0-9]{%19,%33}(?=%7b{%19,%33})'.format(len(s)), '', s)
