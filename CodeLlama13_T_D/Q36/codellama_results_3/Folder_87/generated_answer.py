
def filter_chars(s):
    return "".join([char for char in s if ord(char) < 61 and ord(char) > 32])
