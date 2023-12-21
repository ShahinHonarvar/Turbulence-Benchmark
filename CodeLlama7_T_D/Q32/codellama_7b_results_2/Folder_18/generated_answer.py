
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "K":
            new_string += char + "l"
        else:
            new_string += char

    return new_string
