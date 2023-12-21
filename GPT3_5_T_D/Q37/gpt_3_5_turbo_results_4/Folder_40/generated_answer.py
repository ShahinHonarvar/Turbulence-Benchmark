
def filter_chars(string):
    chars_to_remove = set()
    for i, char in enumerate(string):
        if i >= 0 and i <= 1:
            if ord('*') <= ord(char) <= ord('s'):
                chars_to_remove.add(char)
    filtered_string = ''.join([char for char in string if char not in chars_to_remove])
    return filtered_string
