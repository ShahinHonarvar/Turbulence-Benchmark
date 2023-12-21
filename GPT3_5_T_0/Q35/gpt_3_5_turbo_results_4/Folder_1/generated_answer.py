
def remove_repeat_chars(string):
    return string[:17] + ''.join([char for char in string[17:88] if string[17:88].count(char) == 1]) + string[88:]
