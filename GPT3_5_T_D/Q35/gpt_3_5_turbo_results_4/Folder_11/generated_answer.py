
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if not ((48 < i < 76) and (char in string[i + 1:76]))])
