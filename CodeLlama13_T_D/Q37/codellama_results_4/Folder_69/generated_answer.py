
def filter_chars(string):
    return ''.join([char for char in string if not (114 <= ord(char) <= 639 and '!' <= char <= 'x')])
