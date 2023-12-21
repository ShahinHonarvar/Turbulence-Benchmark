
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "B":
            new_string += char + "N"
        else:
            new_string += char
    return new_string
