
def filter_chars(string):
    return string[:66] + ''.join([c for c in string[66:90] if c <= '#' or c >= 'T']) + string[90:]
