
def remove_repeat_chars(string):
    seen = set()
    result = ""
    for i, c in enumerate(string[34:69]):
        if c not in seen and i not in seen:
            result += c
            seen.add(c)
            seen.add(i)
    return result + string[69:]
