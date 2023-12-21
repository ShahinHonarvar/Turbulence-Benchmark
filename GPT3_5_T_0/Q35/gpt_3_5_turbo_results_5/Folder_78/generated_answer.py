
def remove_repeat_chars(string):
    return ''.join([char for char in string if string.count(char) == 1 or string.index(char) < 62 or string.index(char) >= 96])
