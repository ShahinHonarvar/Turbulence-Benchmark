
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "o":
            new_string += "o"
        new_string += string[i]
    return new_string
