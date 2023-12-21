
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(50, 200):
        if s[i] not in seen:
            seen.add(s[i])
            result.append(s[i])
    return ''.join(result)
