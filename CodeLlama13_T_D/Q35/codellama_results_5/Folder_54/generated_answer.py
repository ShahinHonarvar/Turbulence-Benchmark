
def remove_repeat_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 35 or i > 64:
            result.append(c)
        elif c not in s[i+1:]:
            result.append(c)
    return ''.join(result)
