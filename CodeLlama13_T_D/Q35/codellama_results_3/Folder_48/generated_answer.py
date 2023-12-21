
def remove_repeat_chars(string):
    seen = set()
    result = ""
    for char in string[409:502]:
        if char not in seen:
            result += char
            seen.add(char)
    return result + string[502:]
