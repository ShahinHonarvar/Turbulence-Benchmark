
def filter_chars(string):
    return ''.join(char for char in string if not (32 <= ord(char) <= 46 and '0' <= char <= 'k'))
