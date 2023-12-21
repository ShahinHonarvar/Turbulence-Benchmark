
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 45 or i >= 57 or not ('F' < char < 'n')])
