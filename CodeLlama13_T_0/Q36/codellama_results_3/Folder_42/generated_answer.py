
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] > "t" and string[i] < "x":
            continue
        else:
            new_str += string[i]
    return new_str
