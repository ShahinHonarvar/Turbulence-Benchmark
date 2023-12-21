
def filter_chars(string):
    return string[:56] + ''.join([c for c in string[56:86] if not ('+' < c < 'w')]) + string[86:]
