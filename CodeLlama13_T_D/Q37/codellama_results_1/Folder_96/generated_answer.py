
def filter_chars(string):
    return ''.join([char for char in string if not (ord('!') <= ord(char) <= ord('s') and 86 <= ord(char) <= 92)])
