
def remove_repeat_chars(string):
    seen = set()
    result = ""
    for char in string:
        if char not in seen and len(seen) < 8:
            seen.add(char)
            result += char
    return result
