
def remove_repeat_chars(string):
    return ''.join([char for char in string if string[:2].count(char) <= 1])
