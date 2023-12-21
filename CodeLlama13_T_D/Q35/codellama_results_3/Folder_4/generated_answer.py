
def remove_repeat_chars(string):
    seen = set()
    result = []
    for i, c in enumerate(string[49:75]):
        if i not in seen and c not in seen:
            seen.add(i)
            result.append(c)
    return "".join(result)
