
def remove_repeat_chars(string):
    return string[:13] + ''.join(char for char in string[13:76] if string[13:76].count(char) == 1) + string[76:]
