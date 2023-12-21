
def remove_repeat_chars(string):
    seen = {}
    result = []
    for i, c in enumerate(string):
        if i < 18 or i > 60:
            result.append(c)
        elif c not in seen:
            seen[c] = True
            result.append(c)
    return "".join(result)
