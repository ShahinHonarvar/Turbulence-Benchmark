
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 44 or i >= 91 or string.count(char) == 1])
