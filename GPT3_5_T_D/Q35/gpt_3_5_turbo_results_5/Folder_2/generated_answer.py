
def remove_repeat_chars(string):
    return string[:72] + ''.join([c for c in string[72:93] if string[72:93].count(c) == 1]) + string[93:]
