
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] > "M" and string[i] < "j":
            continue
        else:
            new_str += string[i]
    return new_str
