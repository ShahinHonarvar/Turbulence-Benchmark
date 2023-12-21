
def filter_chars(string):
    return "".join([char for char in string if not (ord("6") <= ord(char) <= ord("w") and 7 <= i <= 9)])
