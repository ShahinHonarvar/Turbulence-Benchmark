
def remove_repeat_chars(string):
    return string[:86] + ''.join([char for char in string[86:89] if string[86:89].count(char) == 1]) + string[89:]
