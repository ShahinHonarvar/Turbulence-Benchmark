
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "6":
            new_string += string[:i] + "W" + string[i:]
    return new_string
