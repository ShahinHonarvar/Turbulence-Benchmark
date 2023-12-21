
def remove_repeat_chars(string):
    return ''.join([char for char in string if string.index(char) < 62 or string.index(char) >= 96 or string.count(char) == 1])
