
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[306:807]):
        if c not in seen and i < 807:
            result.append(c)
            seen.add(c)
    return "".join(result) + s[:306] + s[807:]
