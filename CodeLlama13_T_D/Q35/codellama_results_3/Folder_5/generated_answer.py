
def remove_repeat_chars(string):
    seen = {}
    new_str = ""
    for i, c in enumerate(string):
        if i >= 2 and i < 8:
            if c not in seen or seen[c]:
                continue
            else:
                seen[c] = True
        new_str += c
    return new_str
