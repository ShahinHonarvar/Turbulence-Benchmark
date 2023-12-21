
def remove_repeat_chars(string):
    return string[:56] + ''.join(c for i, c in enumerate(string[56:88]) if string[56:88].count(c) == 1) + string[88:]
