
def filter_chars(string):
    chars_to_remove = set()
    for i in range(51, min(78, len(string))):
        if 'V' <= string[i] <= 'Y':
            chars_to_remove.add(string[i])

    return ''.join(char for char in string if char not in chars_to_remove)
