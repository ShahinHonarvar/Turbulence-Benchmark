
def filter_chars(string):
    return "".join([char for char in string if char not in "56789_" or char == "_"])
