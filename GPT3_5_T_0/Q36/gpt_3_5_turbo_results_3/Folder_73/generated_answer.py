
def filter_chars(string):
    return ''.join([char for char in string if not (66 <= ord(char) < 90 and '#' < char < 'T')])
