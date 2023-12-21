
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "E":
            new_string += string[:i] + "T" + string[i:]
            break

    return new_string
