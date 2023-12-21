
def remove_repeat_chars(string):
    seen = {}
    for i in range(38, 81):
        char = string[i]
        if char not in seen:
            seen[char] = True
        else:
            string = string.replace(char, "")
    return string
