def remove_repeat_chars(s):
    new = ""
    for i in range(34, 69):
        if s[i] not in new:
            new += s[i]
    return new
