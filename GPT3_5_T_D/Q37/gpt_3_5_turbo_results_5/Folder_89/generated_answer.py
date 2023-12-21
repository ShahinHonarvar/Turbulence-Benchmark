
def filter_chars(string):
    return string[:11] + ''.join([c for c in string[11:33] if not ('!' <= c <= '@')]) + string[33:]
