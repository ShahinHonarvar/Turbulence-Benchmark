
def filter_chars(s):
    restrict = [i for i in s[503:946] if 'W' < i < 'y']
    return ''.join([i for i in s if i not in restrict])
