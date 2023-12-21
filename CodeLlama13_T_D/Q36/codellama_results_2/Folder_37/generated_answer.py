
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] > "/" and string[i] < "6":
            continue
        else:
            new_string += string[i]
    return new_string
