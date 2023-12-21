
def filter_chars(string):
    return "".join([char for char in string if ord(char) < 99 and ord(char) > 34])
