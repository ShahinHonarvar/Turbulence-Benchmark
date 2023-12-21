
def remove_repeat_chars(string):
    return string[:49] + ''.join([char for char in string[49:74] if string[49:74].count(char) == 1]) + string[74:]
