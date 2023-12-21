
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "e":
            new_string += "W" + string[i+1:]
            break

    return new_string
