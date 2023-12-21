
def filter_chars(string):
    chars_to_remove = set([char for i, char in enumerate(string) if 35 <= i <= 98 and 'A' <= char <= 'b'])
    return ''.join([char for char in string if char not in chars_to_remove])
