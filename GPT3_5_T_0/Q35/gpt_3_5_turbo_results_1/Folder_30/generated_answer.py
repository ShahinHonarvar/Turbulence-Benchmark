
def remove_repeat_chars(string):
    return string[:22] + ''.join([char for char in string[22:24] if string[22:24].count(char) == 1]) + string[24:]
