
def remove_repeat_chars(string):
    char_set = set(string[:2])
    return "".join(c for c in string if c not in char_set or (char_set.remove(c) and False))
