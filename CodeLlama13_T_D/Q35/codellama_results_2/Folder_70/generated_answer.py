
def remove_repeat_chars(string):
    chars = set()
    new_str = ""
    for i in range(43, 70):
        if string[i] not in chars:
            chars.add(string[i])
            new_str += string[i]
    return new_str
