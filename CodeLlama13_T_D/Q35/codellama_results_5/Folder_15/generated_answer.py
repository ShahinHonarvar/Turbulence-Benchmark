
def remove_repeat_chars(string):
    seen = {}
    result = ""
    for char in string:
        if char in seen and seen[char] <= 4:
            continue
        else:
            seen[char] = seen.get(char, 0) + 1
            result += char
    return result
