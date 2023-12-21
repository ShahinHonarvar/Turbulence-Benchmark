
def remove_repeat_chars(string):
    return string[:72] + ''.join([char for char in string[72:93] if string[72:93].count(char) == 1]) + string[93:]
