
def filter_chars(string):
    for i in range(19, 23):
        if i >= len(string):
            break
        char = string[i]
        if char >= "]" and char <= "t":
            string = string.replace(char, "")
    return string
