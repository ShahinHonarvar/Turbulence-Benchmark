
def remove_repeat_chars(string):
    chars = {}
    for i in range(27, 96):
        if string[i] in chars:
            del chars[string[i]]
        else:
            chars[string[i]] = 1
    return ''.join([c for c in string if c not in chars])
