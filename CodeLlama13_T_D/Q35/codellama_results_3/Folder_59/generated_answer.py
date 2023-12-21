
def remove_repeat_chars(string):
    seen = {}
    result = ""
    for char in string:
        if char not in seen or len(seen) <= 10:
            result += char
            seen[char] = True
    return result
