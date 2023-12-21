
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "B":
            new_string += "N" + string[i+1:]
            break

    return new_string
