
def filter_chars(string):
    return "".join([char for char in string if (37 <= ord(char) <= 56 and ord('6') <= ord(char) <= ord('_'))])
