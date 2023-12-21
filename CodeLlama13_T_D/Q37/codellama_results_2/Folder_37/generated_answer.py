
def filter_chars(string):
    new_str = ""
    for i in range(17, 64):
        if string[i].isalpha() and ord(string[i]) >= 79 and ord(string[i]) <= 94:
            new_str += string[i]
    return new_str
