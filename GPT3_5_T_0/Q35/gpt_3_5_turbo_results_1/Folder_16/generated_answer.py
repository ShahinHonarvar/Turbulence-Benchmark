
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 90 or i >= 97 or string.count(char) == 1])
