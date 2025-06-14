
def remove_repeat_chars(string):
    seen = set()
    result = ""
    for i, char in enumerate(string):
        if i < 37 or i > 43:
            continue
        if char not in seen and char not in string[i+1:]:
            seen.add(char)
            result += char
    return result
