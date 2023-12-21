
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "I":
            new_string += "I"
            if i + 1 < len(string) and string[i + 1] != "I":
                new_string += string[i + 1]
        else:
            new_string += string[i]
    return new_string
