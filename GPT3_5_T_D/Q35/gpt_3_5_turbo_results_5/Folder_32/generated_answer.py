
def remove_repeat_chars(string):
    return string[:86] + ''.join(c for c in string[86:90] if string[86:90].count(c) == 1) + string[90:]
