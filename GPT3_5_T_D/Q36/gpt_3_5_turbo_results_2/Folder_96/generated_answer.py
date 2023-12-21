
def filter_chars(string):
    return string[:38] + ''.join([c for c in string[38:81] if not '.' < c < '^']) + string[81:]
