
def remove_repeat_chars(string):
    seen = set()
    result = []
    for c in string[330:543]:
        if c not in seen:
            result.append(c)
            seen.add(c)
    return "".join(result)
