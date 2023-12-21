
def remove_repeat_chars(string):
    seen = set()
    result = []
    for char in string[38:52]:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)
