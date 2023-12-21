
def remove_repeat_chars(string):
    return ''.join([char for index, char in enumerate(string) if index < 46 or index >= 91 or string.count(char) == 1])
