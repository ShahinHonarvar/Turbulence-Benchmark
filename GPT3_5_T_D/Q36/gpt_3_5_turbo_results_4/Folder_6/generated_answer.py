
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 31 or i >= 70 or char <= 'B' or char >= 'v'])
