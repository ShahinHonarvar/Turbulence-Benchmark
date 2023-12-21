
def remove_repeat_chars(string):
    chars = {}
    for i, c in enumerate(string[90:200]):
        if c not in chars or chars[c]:
            continue
        chars[c] = True
        string = string.replace(c, '')
    return string
