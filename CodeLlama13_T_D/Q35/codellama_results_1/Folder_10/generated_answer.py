
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[36:54]):
        if i not in seen and c not in seen:
            seen.add(i)
            seen.add(c)
            result.append(c)
    return "".join(result)
