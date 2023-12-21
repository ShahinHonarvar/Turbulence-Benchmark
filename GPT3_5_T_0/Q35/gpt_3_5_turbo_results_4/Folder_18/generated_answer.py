
def remove_repeat_chars(string):
    return string[:56] + ''.join([char for char in string[56:90] if string[56:90].count(char) == 1]) + string[90:]
