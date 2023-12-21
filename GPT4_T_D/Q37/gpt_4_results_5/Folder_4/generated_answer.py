
def filter_chars(string):
    index_chars = set(string[19:34])
    char_range = set(chr(i) for i in range(ord('S'), ord('{')+1))
    chars_to_remove = index_chars.intersection(char_range)
    return ''.join(char for char in string if char not in chars_to_remove)
