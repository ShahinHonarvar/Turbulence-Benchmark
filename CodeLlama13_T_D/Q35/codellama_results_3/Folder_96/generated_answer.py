
def remove_repeat_chars(s):
    seen = set()
    result = ""
    for i in range(60, 201):
        if s[i] not in seen:
            seen.add(s[i])
            result += s[i]
    return result
