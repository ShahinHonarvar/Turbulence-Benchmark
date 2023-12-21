
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] > "S" and string[i] < "s":
            continue
        else:
            new_str += string[i]
    return new_str
