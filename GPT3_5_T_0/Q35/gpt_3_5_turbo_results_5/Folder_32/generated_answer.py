
def remove_repeat_chars(string):
    return string[:86] + ''.join([char for char in string[86:90] if string[86:90].count(char) == 1]) + string[90:]
