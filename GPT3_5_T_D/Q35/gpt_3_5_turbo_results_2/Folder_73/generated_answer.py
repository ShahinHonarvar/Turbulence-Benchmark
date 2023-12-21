
def remove_repeat_chars(string):
    return string[:10] + ''.join([char for char in string[10:76] if string[10:76].count(char) == 1]) + string[76:]
