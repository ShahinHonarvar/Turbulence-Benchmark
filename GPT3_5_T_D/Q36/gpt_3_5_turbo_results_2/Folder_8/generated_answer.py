
def filter_chars(string):
    return string[:82] + ''.join([c for c in string[82:93] if not ('!' < c < '*')]) + string[93:]
