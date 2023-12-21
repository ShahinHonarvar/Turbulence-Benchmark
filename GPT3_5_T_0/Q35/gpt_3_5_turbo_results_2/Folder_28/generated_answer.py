
def remove_repeat_chars(string):
    return string[:86] + ''.join([char for char in string[86:99] if string[86:99].count(char) == 1]) + string[99:]
