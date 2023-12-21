
def filter_chars(string):
    return string[:502] + ''.join(c for c in string[502:946] if not ('W' < c < 'y')) + string[946:]
