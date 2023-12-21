
def remove_repeat_chars(string):
    return string[:44] + ''.join([char for char in string[44:78] if string[44:78].count(char) == 1]) + string[78:]
