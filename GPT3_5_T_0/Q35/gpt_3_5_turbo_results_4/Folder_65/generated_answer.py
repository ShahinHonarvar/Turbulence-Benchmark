
def remove_repeat_chars(string):
    return string[:51] + ''.join([char for char in string[51:76] if string[51:76].count(char) == 1]) + string[76:]
