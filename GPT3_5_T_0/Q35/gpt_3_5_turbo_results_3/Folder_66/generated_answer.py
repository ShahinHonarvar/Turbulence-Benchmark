
def remove_repeat_chars(string):
    return string[:11] + ''.join([char for char in string[11:76] if string[11:76].count(char) == 1]) + string[76:]
