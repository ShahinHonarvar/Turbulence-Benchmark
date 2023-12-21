
def remove_repeat_chars(s):
    seen = set()
    new_str = ''
    for i, c in enumerate(s[306:807]):
        if c not in seen and i != 306:
            seen.add(c)
            new_str += c
    return s[:305] + new_str + s[807:]
