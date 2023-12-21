
def filter_chars(string):
    for i in range(46, 91):
        if string[i].isalpha() and string[i] > "D" and string[i] < "H":
            string = string.replace(string[i], "")
    return string
