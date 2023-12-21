
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if 90 < i < 97 or string.count(char) == 1])
