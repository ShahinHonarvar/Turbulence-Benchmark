
def filter_chars(string):
    return "".join([char for char in string if ord("m") < ord(char) < ord("w")])
