
def remove_repeat_chars(string):
    return string[:2] + ''.join([c for c in string[2:7] if string[2:7].count(c) == 1]) + string[7:]
