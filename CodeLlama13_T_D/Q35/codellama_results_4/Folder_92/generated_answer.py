
def remove_repeat_chars(string):
    seen = set()
    new_string = ""
    for char in string:
        if char not in seen and len(seen) < 2:
            seen.add(char)
            new_string += char
    return new_string
