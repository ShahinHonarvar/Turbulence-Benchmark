
def filter_chars(string):
    return string[:46] + ''.join(c for c in string[46:74] if c <= '&' or c >= 'M') + string[74:]
