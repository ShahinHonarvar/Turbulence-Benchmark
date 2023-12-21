
def filter_chars(string):
    return "".join([char for char in string if ord(char) < 77 or ord(char) > 109])
