
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 81 or i >= 86 or char not in string[81:86]])
