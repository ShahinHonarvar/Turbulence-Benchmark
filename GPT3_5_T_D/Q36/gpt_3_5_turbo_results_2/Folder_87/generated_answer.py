
def filter_chars(string):
    return ''.join(char for char in string if not ('3' < char < 'D' and 32 <= ord(char) < 61))
