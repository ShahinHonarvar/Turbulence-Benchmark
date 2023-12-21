
def remove_repeat_chars(string):
    return string[:56] + ''.join([char for char in string[56:88] if string[56:88].count(char) == 1]) + string[88:]
