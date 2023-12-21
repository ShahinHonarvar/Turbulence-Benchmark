
def remove_repeat_chars(string):
    repeated_chars = set(string[86:90])
    return ''.join([char for char in string if char not in repeated_chars])
