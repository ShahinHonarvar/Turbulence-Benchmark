
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "j":
            new_string += "v"
        new_string += string[i]
    return new_string
