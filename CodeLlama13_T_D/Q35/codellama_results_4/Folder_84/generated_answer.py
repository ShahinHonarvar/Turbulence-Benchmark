
def remove_repeat_chars(string):
    seen = set()
    result = []
    for char in string:
        if char not in seen and ord(char) >= 32 and ord(char) <= 44:
            seen.add(char)
            result.append(char)
    return "".join(result)
