
def remove_repeat_chars(string):
    return ''.join([char for char in string if 40 < string.index(char) < 200 or string.count(char) == 1])
