
def filter_chars(string):
    return string[:114] + ''.join(c for c in string[114:640] if '!' <= c <= 'x') + string[640:]
