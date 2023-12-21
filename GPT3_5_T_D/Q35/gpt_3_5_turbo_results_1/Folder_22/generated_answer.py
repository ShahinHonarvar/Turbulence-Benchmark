
def remove_repeat_chars(string):
    return string[:50] + ''.join([c for i, c in enumerate(string[50:200]) if string.index(c) == i]) + string[200:]
