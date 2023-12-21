
def filter_chars(string):
    return ''.join([char for char in string if not (48 <= ord(char) < 75 and '6' < char < '_')])
