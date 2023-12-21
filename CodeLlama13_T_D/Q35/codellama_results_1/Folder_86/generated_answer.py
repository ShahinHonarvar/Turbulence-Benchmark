
def remove_repeat_chars(string):
    seen = set()
    result = []
    for char in string[19:32]:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return "".join(result)
