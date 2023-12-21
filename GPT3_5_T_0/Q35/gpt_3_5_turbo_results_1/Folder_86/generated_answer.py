
def remove_repeat_chars(string):
    return string[:19] + ''.join([char for char in string[19:32] if string[19:32].count(char) == 1]) + string[32:]
