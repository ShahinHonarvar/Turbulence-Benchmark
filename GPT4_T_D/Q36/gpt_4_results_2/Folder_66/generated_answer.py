
def filter_chars(s):
    charset = set([c for c in s[40:87] if '!' < c < '}'])
    return ''.join([c for c in s if c not in charset])
