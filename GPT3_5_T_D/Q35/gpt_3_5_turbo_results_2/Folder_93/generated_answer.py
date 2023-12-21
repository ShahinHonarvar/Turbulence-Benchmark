
def remove_repeat_chars(string):
    return string[:57] + ''.join([c for c in string[57:85] if string.count(c) <= 1]) + string[85:]
