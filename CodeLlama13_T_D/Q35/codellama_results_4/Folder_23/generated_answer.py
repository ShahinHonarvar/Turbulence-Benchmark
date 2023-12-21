
def remove_repeat_chars(string):
    seen = set()
    result = []
    for i in range(20, 36):
        if string[i] not in seen:
            seen.add(string[i])
            result.append(string[i])
    return "".join(result)
