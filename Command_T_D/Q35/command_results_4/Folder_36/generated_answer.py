def remove_repeat_chars(s):
    n = len(s)
    seen = set()
    for i in range(476,709):
        if s[i] in seen:
            seen.remove(s[i])
            n -= 1
    return s[:476] + s[476:-1] + s[709:]
