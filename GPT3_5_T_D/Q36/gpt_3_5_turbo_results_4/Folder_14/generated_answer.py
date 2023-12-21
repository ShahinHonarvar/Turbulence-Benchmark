
def filter_chars(string):
    return string[:41] + ''.join([char for char in string[41:56] if not ('Z' < char < 'c')]) + string[56:]
