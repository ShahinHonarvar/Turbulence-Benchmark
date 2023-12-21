
def remove_repeat_chars(string):
    return string[:51] + ''.join([c for c in string[51:76] if string.count(c) == 1]) + string[76:]
