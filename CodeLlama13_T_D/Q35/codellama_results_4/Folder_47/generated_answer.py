
def remove_repeat_chars(string):
    seen = set()
    new_str = ""
    for char in string[29:53]:
        if char not in seen:
            seen.add(char)
            new_str += char
    return new_str + string[53:]
