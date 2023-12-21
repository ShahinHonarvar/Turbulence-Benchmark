
def filter_chars(s):
    new_string = ""
    for i in range(27, 75):
        if s[i] > "A" and s[i] < "i":
            new_string += s[i]
    return new_string
