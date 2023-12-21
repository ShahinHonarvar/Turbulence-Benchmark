
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 348 or i > 852 or not 'J' <= char <= 'b'])
