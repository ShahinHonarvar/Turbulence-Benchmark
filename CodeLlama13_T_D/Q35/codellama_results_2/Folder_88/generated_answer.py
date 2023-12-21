
def remove_repeat_chars(s):
    seen = set()
    result = ""
    for i, c in enumerate(s):
        if i < 3 or i > 9:
            result += c
        elif c not in seen:
            result += c
            seen.add(c)
    return result
