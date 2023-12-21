
def filter_chars(string):
    chars = []
    for i, char in enumerate(string):
        if 20 <= i <= 79 and '!' <= char <= 'T':
            chars.append(char)
    return ''.join([char for char in string if char not in chars])
