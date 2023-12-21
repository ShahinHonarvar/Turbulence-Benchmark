
def remove_repeat_chars(string):
    return ''.join([char for char in string if string.index(char) < 69 or string.index(char) >= 97 or string.count(char) == 1])
