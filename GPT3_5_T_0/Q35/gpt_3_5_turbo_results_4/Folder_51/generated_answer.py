
def remove_repeat_chars(string):
    return string[:6] + ''.join([char for char in string[6:9] if string[6:9].count(char) == 1]) + string[9:]
