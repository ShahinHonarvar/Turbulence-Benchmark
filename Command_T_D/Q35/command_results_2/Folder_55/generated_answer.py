def remove_repeat_chars(s):
    new = ""
    for i in range(10, 100):
        if s[i] not in new:
            new += s[i]
    return new
