
def filter_chars(s):
    chars_in_range = set([char for index, char in enumerate(s) if 25 <= index <= 97 and 'm' <= char <= 'w'])
    altered_s = ''.join(char for char in s if char not in chars_in_range)
    return altered_s
