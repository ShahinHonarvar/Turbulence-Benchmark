
def remove_repeat_chars(string):
    return string[:34] + ''.join([char for i, char in enumerate(string[34:69]) if string[34:69].count(char) == 1]) + string[69:]
