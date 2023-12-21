
def filter_chars(string):
    return string[:39] + ''.join(c for c in string[39:87] if c <= '!' or c >= '}') + string[87:]
