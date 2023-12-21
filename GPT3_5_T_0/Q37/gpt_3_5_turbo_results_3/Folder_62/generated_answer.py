
def filter_chars(string):
    return string[:10] + string[70:] + ''.join(c for c in string[10:70] if c < 'I' or c > 'K')
