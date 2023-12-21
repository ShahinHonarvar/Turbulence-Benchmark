
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for c in s:
        if ord(c) < 90 or ord(c) > 97:
            result += c
        elif c not in seen:
            result += c
            seen.add(c)
    return result
