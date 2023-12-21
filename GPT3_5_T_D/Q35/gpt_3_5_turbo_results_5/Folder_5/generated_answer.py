
def remove_repeat_chars(string):
    return string[:2] + ''.join([c for c in string[2:8] if string[2:8].count(c) == 1]) + string[8:]
