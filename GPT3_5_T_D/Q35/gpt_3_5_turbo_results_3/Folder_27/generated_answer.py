
def remove_repeat_chars(string):
    count = {}
    for c in string:
        count[c] = count.get(c, 0) + 1
    new_string = ""
    for i, c in enumerate(string):
        if 86 < i < 89 and count.get(c, 0) > 1:
            continue
        new_string += c
    return new_string
