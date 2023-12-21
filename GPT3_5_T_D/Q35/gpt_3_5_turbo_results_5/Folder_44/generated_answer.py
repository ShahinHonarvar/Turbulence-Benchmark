
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 36 or i >= 52 or string[36:i].count(char) < 1])
