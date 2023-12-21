
def remove_repeat_chars(string):
    repeat_chars = [char for char in string[11:79] if string[11:79].count(char) > 1]
    return ''.join(char for char in string if char not in repeat_chars)
