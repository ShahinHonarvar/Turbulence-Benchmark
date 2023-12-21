
def filter_chars(str):
    filter_chars = set([char for i, char in enumerate(str) if 32 <= i <= 46 and '0' <= char <= 'k'])
    return ''.join([char for char in str if char not in filter_chars]) 
