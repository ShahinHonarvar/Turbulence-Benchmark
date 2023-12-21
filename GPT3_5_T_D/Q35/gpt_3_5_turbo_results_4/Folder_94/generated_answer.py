
def remove_repeat_chars(string):
    return string[:42] + ''.join([char for char in string[42:87] if string[42:87].count(char) == 1]) + string[87:]
