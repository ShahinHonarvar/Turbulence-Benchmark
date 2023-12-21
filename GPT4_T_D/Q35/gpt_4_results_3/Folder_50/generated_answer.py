
def remove_repeat_chars(string):
    repeat_chars = [char for char in string[14:76] if string[14:76].count(char) > 1]
    return ''.join(char for char in string if char not in repeat_chars)
