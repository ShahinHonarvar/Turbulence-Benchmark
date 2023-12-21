
def filter_chars(string):
    return string[:77] + ''.join(c for c in string[77:87] if not (';' < c < 'r')) + string[87:]
