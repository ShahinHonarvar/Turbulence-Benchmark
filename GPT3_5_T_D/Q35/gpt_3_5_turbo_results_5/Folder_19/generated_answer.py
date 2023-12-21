
def remove_repeat_chars(string):
    unique_chars = set(string[1:4])
    return ''.join([char for char in string if char not in unique_chars or string[1:4].count(char) == 1])
