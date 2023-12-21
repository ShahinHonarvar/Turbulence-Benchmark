
def remove_repeat_chars(string):
    return string[:125] + ''.join([char for char in string[125:825] if string[125:825].count(char) == 1]) + string[825:]
