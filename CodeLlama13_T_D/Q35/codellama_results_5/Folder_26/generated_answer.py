
def remove_repeat_chars(string):
    seen = set()
    for i in range(68, 99):
        char = string[i]
        if char not in seen:
            seen.add(char)
        else:
            string = string.replace(char, "")
    return string
