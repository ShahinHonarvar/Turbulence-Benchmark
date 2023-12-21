
def remove_repeat_chars(string):
    return string[:81] + ''.join([char for char in string[81:86] if string[81:86].count(char) == 1]) + string[86:]
