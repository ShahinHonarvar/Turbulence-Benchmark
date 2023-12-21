
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[90:200]):
        if c not in seen and i < 200:
            result.append(c)
            seen.add(c)
    return "".join(result) + s[:90] + s[200:]
