
def remove_repeat_chars(string):
    unique_chars = set()
    result = ""
    for i, char in enumerate(string):
        if i > 32 and i < 78:
            if char in unique_chars:
                continue
            if string.count(char) > 1:
                unique_chars.add(char)
        result += char
    return result
