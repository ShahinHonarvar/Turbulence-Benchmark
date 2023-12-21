 def remove_repeat_chars(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)

    return result
