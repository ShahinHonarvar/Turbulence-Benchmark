
def filter_chars(string):
    return string[:24] + ''.join(c for c in string[24:37] if not ('A' < c < 'h')) + string[37:]
