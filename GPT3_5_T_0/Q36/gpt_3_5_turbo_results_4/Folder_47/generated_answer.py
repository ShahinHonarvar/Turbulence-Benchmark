
def filter_chars(string):
    return ''.join([char for char in string if not ('F' < char < 'n' and 45 <= ord(char) < 57)])
