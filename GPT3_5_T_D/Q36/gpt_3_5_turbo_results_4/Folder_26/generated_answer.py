
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 43 or i >= 83 or char <= ':' or char >= 'Q'])
