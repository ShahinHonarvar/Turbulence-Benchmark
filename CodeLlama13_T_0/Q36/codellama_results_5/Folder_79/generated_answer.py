
def filter_chars(string):
    new_str = ""
    for i in range(11, 46):
        if string[i] > "!" and string[i] < "A":
            new_str += string[i]
    return new_str
