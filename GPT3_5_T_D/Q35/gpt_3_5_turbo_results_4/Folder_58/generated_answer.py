
def remove_repeat_chars(string):
    return ''.join([char for index, char in enumerate(string) if index < 103 or index >= 802 or string.count(char) == 1])
