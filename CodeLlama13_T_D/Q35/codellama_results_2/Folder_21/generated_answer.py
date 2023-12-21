
def remove_repeat_chars(string):
    seen = set()
    result = []
    for char in string[462:995]:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)
