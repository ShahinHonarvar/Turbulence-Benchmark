
def filter_chars(string):
    return ''.join(char for char in string if not ('m' < char < 'w') or not 32 <= ord(char) < 84)
