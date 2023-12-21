
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if (i < 81 or i > 86) or string[i].isalpha() == False:
            new_string += string[i]
        else:
            new_string += ""
    return new_string
