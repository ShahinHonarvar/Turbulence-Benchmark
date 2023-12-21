
def remove_repeat_chars(string):
    return string[:44] + ''.join([c for c in string[44:78] if string[44:78].count(c) == 1]) + string[78:]
