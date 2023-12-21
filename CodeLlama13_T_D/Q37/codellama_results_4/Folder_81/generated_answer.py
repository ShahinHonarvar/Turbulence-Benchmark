
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i].isalpha() and ord(string[i]) >= 8 and ord(string[i]) <= 120:
            new_str += string[i]
    return new_str
