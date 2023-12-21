
def filter_chars(string):
    return string[:344] + ''.join(c for c in string[344:874] if c <= 'f' or c >= '~') + string[874:]
