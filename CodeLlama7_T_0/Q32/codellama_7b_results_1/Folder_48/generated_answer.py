
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "S":
            new_string += "SU"
        else:
            new_string += string[i]
    return new_string
