
def filter_chars(string):
    return ''.join([char for char in string if not (90 < ord(char) < 97 and 'j' < char < 'w')])
