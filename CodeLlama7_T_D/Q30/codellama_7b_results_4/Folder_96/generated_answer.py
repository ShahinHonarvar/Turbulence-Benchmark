
def insert_before_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "A":
            new_string += "a"
        else:
            new_string += char

    return new_string
