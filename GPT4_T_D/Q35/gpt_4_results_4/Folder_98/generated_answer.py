
def remove_repeat_chars(string):
    repeats = [char for char in string[1:7] if string[1:7].count(char) > 1]
    result = ''.join([char for char in string if char not in repeats])
    return result
