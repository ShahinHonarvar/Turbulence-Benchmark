
def filter_chars(string):
    return ''.join([char for char in string if not ('I' < char < 'a' and 49 <= ord(char) < 56)])
