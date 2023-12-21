
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if 60 <= i < 200 or string.count(char) == 1])
