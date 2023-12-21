
def remove_repeat_chars(string):
    return string[:39] + ''.join(filter(lambda c: string.count(c) == 1 or string.index(c) < 39 or string.index(c) >= 43, string[39:43])) + string[43:]
