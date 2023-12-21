
def filter_chars(string):
    return string[:23] + ''.join([c for c in string[23:45] if not ('3' < c < 'I')]) + string[45:]
