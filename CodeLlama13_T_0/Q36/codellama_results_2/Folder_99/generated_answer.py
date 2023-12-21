
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] > "b" and string[i] < "d":
            continue
        else:
            new_str += string[i]
    return new_str
