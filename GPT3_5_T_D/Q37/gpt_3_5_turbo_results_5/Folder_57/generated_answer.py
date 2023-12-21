
def filter_chars(string):
    return string[:27] + ''.join(c for c in string[27:86] if not ('!' <= c <= 'B')) + string[86:]
