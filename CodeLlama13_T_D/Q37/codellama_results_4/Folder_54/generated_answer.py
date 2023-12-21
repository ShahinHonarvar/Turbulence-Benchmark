
def filter_chars(string):
    return "".join([char for char in string if not (46 <= ord(char) <= 85 and '-' <= char <= 'X')])
