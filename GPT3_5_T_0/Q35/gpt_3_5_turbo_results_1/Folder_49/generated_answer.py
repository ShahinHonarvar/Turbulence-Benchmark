
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 90 or i >= 200 or string[90:i].count(char) == 1])
