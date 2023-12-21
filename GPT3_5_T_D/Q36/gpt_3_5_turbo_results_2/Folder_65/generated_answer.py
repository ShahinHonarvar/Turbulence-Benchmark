
def filter_chars(string):
    return string[:58] + ''.join(c for c in string[58:82] if not ('F' < c < 'O')) + string[82:]
