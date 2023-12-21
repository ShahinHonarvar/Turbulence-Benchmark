
def remove_repeat_chars(string):
    return ''.join([char for char in string if string[27:96].count(char) <= 1])
