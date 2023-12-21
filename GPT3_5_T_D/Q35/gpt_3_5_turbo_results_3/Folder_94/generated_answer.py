
def remove_repeat_chars(string):
    return string[:42] + ''.join([c for c in string[42:87] if string[42:87].count(c) == 1]) + string[87:]
