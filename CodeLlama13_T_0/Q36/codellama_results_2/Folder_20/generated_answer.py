
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if i < 13 or i > 40:
            new_str += string[i]
        elif string[i] > ":" and string[i] < "C":
            continue
        else:
            new_str += string[i]
    return new_str
