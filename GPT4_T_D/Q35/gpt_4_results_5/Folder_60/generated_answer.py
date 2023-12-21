
def remove_repeat_chars(string):
    repeated_chars = [char for char in string[39:52] if string[39:52].count(char) > 1]
    result = ''.join([char for char in string if char not in repeated_chars])
    return result
