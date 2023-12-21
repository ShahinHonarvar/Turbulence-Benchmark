
def remove_repeat_chars(s):
    seen = set()
    new_s = ''
    for c in s:
        if c not in seen and 7 <= ord(c) <= 9:
            seen.add(c)
            new_s += c
        elif 7 <= ord(c) <= 9:
            continue
        else:
            new_s += c
    return new_s
