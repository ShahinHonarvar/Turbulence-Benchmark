
def filter_chars(string):
    for i in range(81, 90):
        if string[i].isalpha() and string[i].lower() > "f" and string[i].lower() < "{":
            string = string.replace(string[i], "")
    return string
