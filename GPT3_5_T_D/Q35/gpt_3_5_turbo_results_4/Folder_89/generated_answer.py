
def remove_repeat_chars(string):
    return string[:55] + ''.join([char for char in string[55:84] if string[55:84].count(char) == 1]) + string[84:]
