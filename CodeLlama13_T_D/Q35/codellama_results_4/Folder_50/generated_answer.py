
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for c in s[13:76]:
        if c not in seen:
            result += c
            seen.add(c)
    return result
