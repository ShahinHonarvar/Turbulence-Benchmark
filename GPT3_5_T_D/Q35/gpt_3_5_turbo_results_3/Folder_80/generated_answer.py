
def remove_repeat_chars(string):
    return string[:57] + ''.join([c for c in string[57:84] if string[57:84].count(c) == 1]) + string[84:]
