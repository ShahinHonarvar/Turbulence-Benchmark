
def remove_repeat_chars(string):
    return string[:68] + ''.join([c for i, c in enumerate(string[68:99]) if string[68:99].count(c) == 1]) + string[99:]
