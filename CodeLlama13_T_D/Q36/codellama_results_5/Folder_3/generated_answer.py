
def filter_chars(string):
    new_string = ""
    for i in range(42, 78):
        if string[i] > "!" and string[i] < "?":
            new_string += string[:i] + string[i+1:]
        else:
            new_string += string[i]
    return new_string
