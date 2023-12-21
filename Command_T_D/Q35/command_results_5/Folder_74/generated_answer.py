def remove_repeat_chars(s):
    result = []
    for c in s[69:-97]:
        if c not in result:
            result += [c]
    return ''.join(result)
