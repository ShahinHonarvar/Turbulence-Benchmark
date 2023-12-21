
def remove_repeat_chars(string):
    return string[:476] + ''.join([ch for ch in string[476:709] if string[476:709].count(ch) == 1]) + string[709:]
