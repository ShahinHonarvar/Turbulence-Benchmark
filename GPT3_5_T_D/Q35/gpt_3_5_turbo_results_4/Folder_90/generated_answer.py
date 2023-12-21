
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 306 or i >= 807 or string[306:i].count(char) == 1])
