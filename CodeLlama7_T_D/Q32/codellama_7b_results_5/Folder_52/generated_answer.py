
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "T":
            new_string += "V" + string[i+1:]
            break

    return new_string
