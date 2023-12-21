
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == " ":
            new_string += char + "P"
        else:
            new_string += char

    return new_string
