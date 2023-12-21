
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 10 or i >= 79 or string[10:i].count(char) < 2])
