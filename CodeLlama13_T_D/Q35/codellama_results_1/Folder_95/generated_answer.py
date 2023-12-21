
def remove_repeat_chars(string):
    seen = set()
    out = ""
    for i in range(32, 99):
        if string[i] not in seen:
            seen.add(string[i])
            out += string[i]
    return out
