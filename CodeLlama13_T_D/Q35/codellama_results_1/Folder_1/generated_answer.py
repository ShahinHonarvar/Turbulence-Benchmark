
def remove_repeat_chars(string):
    seen = set()
    result = []
    for char in string[17:88]:
        if char not in seen and char not in result:
            result.append(char)
            seen.add(char)
    return "".join(result)
