
def filter_chars(string):
    return ''.join([char for char in string if not (char >= 'E' and char <= '~' and string.index(char) >= 63 and string.index(char) <= 84)])
