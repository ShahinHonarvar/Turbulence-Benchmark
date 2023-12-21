
def remove_repeat_chars(string):
    return string[:39] + ''.join([char for char in string[39:43] if string[39:43].count(char) == 1]) + string[43:]
