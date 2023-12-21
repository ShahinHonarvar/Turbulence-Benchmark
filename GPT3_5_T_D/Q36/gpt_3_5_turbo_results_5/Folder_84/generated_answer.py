
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if 171 <= i < 636:
            if string[i] > "c" and string[i] < "s":
                continue
        new_string += string[i]
    return new_string
