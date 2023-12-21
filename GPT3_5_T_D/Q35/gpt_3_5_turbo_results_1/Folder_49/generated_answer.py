
def remove_repeat_chars(string):
    return ''.join([char for char in string if string.index(char) < 90 or string.index(char) >= 200 or string.count(char) == 1])
