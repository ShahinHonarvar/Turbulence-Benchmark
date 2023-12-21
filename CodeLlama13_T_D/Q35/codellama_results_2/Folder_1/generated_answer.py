
def remove_repeat_chars(string):
    seen = set()
    result = []
    for char in string[17:88]:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)
