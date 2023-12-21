
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 42 or i >= 87 or string.count(char) == 1])
