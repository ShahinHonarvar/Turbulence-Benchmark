
def filter_chars(string):
    new_str = ""
    for i in range(1, 9):
        if string[i] > "8" and string[i] < "m":
            new_str += string[:i] + string[i+1:]
        else:
            new_str += string[i]
    return new_str
