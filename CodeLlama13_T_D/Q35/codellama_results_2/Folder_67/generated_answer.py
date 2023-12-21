
def remove_repeat_chars(s):
    seen = set()
    result = ""
    for c in s[44:67]:
        if c not in seen:
            result += c
            seen.add(c)
    return result
