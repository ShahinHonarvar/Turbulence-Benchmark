
def remove_repeat_chars(string):
    return string[:55] + ''.join([c for c in string[55:84] if string[55:84].count(c) == 1]) + string[84:]
