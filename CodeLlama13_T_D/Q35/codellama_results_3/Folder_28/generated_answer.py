
def remove_repeat_chars(string):
    seen = set()
    new_str = ""
    for char in string[86:99]:
        if char not in seen:
            new_str += char
            seen.add(char)
    return new_str + string[99:]
