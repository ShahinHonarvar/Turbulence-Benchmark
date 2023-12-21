
def filter_chars(string):
    return string[:344] + ''.join(c for c in string[344:874] if not ('f' < c < '~')) + string[874:]
