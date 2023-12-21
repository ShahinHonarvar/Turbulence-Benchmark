
def remove_repeat_chars(string):
    return string[:13] + ''.join([char for char in string[13:70] if string[13:70].count(char) == 1]) + string[70:]
