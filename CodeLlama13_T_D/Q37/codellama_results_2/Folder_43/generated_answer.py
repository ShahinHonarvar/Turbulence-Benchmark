
def filter_chars(string):
    return ''.join([char for char in string if char < '{' and char >= 'W'])
