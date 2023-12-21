
def remove_repeat_chars(s):
    seen = {}
    result = ""
    for i in range(20, 43):
        if s[i] not in seen:
            seen[s[i]] = True
            result += s[i]
    return result
