
def remove_repeat_chars(string):
    return string[:476] + ''.join([char for i, char in enumerate(string[476:709]) if char not in string[476:i+476]]) + string[709:]
