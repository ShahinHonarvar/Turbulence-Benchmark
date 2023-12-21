
def filter_chars(string):
    return string[:14] + ''.join(c for c in string[14:75] if not ('9' < c < 'K')) + string[75:]
