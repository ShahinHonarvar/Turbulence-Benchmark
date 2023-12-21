
def filter_chars(string):
    return string[:323] + ''.join([c for c in string[323:526] if not ')' < c < 'O']) + string[526:]
