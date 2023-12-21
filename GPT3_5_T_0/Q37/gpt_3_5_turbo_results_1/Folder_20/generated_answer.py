
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 25 or i > 97 or char < 'm' or char > 'w'])
