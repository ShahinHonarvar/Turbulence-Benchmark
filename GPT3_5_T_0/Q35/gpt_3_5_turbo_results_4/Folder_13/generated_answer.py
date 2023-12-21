
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 46 or i >= 91 or string[46:i].count(char) == 0])
