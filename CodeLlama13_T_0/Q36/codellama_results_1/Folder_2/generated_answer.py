
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] > "D" and string[i] < "J":
            new_str += string[i]
    return new_str
