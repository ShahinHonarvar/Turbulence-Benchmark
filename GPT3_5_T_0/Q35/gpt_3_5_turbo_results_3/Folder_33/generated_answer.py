
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 125 or i >= 825 or string[125:i].count(char) == 0])
