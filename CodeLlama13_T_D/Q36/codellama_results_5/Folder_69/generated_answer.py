
def filter_chars(s):
    return ''.join([char for char in s if ord(char) < 65 or ord(char) > 90])
