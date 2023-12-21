
def remove_repeat_chars(string):
    seen = set()
    result = ""
    for c in string:
        if c not in seen and len(seen) < 5:
            seen.add(c)
            result += c
    return result
