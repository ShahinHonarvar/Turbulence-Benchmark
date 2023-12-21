
def filter_chars(s):
    filter_set = set(chr for chr in s[477:985] if ',' <= chr <= 'V')
    return ''.join(chr for chr in s if chr not in filter_set)
