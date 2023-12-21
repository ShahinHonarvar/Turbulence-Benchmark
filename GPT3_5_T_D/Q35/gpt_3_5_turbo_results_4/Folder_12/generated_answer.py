
def remove_repeat_chars(string):
    return string[:16] + ''.join([char for char in string[16:87] if string[16:87].count(char) == 1]) + string[87:]
