
def remove_repeat_chars(string):
    return string[:57] + ''.join([c for i, c in enumerate(string[57:85]) if string[57:85].count(c) == 1]) + string[85:]
