
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if string[i].isalpha() and (86 < ord(string[i]) < 93 or 97 < ord(string[i]) < 123):
            continue

        else:

            new_string += string[i]

    return new_string
