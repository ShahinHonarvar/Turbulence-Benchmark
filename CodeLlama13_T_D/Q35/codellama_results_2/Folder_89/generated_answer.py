
def remove_repeat_chars(s):
    new_string = ""
    for i, c in enumerate(s):
        if i < 55 or i > 84:
            new_string += c
        elif s[i - 1] != c and s[i + 1] != c:
            new_string += c
    return new_string
