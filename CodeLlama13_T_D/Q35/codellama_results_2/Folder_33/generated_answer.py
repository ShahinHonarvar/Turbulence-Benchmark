
def remove_repeat_chars(s):
    seen = set()
    new_string = ""
    for c in s[125:825]:
        if c not in seen:
            new_string += c
            seen.add(c)
    return new_string
