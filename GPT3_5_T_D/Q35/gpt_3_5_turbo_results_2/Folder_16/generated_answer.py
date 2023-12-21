
def remove_repeat_chars(string):
    if len(string) < 97:
        return string
    else:
        return ''.join([char for index, char in enumerate(string) if (90 < index < 97) or (string.count(char) == 1)])
