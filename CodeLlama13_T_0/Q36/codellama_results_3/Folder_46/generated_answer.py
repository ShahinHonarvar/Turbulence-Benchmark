
def filter_chars(string):
    new_str = ""
    for i in range(19, 69):
        if string[i] > "<" and string[i] < "C":
            new_str += string[i]
    return new_str
