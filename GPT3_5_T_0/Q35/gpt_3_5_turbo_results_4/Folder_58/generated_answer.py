
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 103 or i >= 802 or string[103:i].count(char) == 1])
