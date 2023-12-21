
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(30, 201):
        if s[i] not in seen:
            result.append(s[i])
            seen.add(s[i])
    return "".join(result)
