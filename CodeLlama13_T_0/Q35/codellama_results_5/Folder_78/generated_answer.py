
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s:
        if c not in seen and 62 < ord(c) < 96:
            seen.add(c)
            result.append(c)
    return "".join(result)
