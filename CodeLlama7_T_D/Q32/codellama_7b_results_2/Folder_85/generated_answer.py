
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "o":
            new_string += char + "a"
        else:
            new_string += char

    return new_string
