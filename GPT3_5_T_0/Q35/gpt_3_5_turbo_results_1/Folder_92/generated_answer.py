
def remove_repeat_chars(string):
    return ''.join([char for char in string if string.index(char) < 2 or string.count(char) == 1])
