
def remove_repeat_chars(string):
    seen = set()
    result = []
    for char in string:
        if char[38:81] and char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)
