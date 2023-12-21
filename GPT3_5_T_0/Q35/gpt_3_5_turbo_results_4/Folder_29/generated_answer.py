
def remove_repeat_chars(string):
    return string[:70] + ''.join([char for char in string[70:98] if string[70:98].count(char) == 1]) + string[98:]
