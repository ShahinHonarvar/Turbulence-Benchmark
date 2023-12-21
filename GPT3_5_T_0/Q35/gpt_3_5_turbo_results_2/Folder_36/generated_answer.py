
def remove_repeat_chars(string):
    return string[:476] + ''.join([char for char in string[476:709] if string[476:709].count(char) == 1]) + string[709:]
