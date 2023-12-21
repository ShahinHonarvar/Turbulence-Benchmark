
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s[200:202]:
        if c not in seen:
            result.append(c)
            seen.add(c)
    return "".join(result) + s[202:]
