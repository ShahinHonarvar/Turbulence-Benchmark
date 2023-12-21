
def filter_chars(string):
    return ''.join([char for char in string if not (603 <= ord(char) <= 759 and 'Q' <= char <= 'h')])
