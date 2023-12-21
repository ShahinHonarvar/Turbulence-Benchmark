
def remove_repeat_chars(str):
    repeated_chars = [char for char in str[37:85] if str[37:85].count(char) > 1]
    return ''.join([char for char in str if char not in repeated_chars])
