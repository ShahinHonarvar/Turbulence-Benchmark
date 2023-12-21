
def filter_chars(string):
    return string[:343] + ''.join(c for c in string[343:665] if not '%' < c < 'U') + string[665:]
