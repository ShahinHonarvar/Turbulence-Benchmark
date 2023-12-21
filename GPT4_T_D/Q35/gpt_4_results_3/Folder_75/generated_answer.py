
def remove_repeat_chars(string):
    repeat_chars = {char for char in string[21:51] if string[21:51].count(char) > 1}
    return ''.join([char for char in string if char not in repeat_chars])
