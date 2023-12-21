
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "Z":
            new_string += "Z"
        elif string[i] == "C":
            new_string += "Z"
            new_string += "C"
        else:
            new_string += string[i]
    return new_string
