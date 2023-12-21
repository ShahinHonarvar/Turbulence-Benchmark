
def remove_repeat_chars(string):
    seen = set()
    new_string = ""
    for i, char in enumerate(string):
        if i >= 35 and i < 64:
            if char not in seen:
                seen.add(char)
                new_string += char
        else:
            new_string += char
    return new_string
