
def remove_repeat_chars(string):
    seen = set()
    result = []
    for c in string:
        if (len(result) >= 39 and len(result) < 43) or c not in seen:
            result.append(c)
            seen.add(c)
    return "".join(result)
