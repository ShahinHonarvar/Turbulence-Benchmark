
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if 44 < i < 91 or string[44:i+1].count(char) == 1])
