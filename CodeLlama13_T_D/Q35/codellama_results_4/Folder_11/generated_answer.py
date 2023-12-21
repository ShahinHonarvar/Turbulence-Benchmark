
def remove_repeat_chars(string):
    seen = set()
    result = ""
    for char in string[48:76]:
        if char not in seen:
            seen.add(char)
            result += char
    return result
