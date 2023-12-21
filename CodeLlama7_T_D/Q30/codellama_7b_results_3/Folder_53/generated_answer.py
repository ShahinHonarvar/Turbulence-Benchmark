
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i].lower() == "i":
            new_string += string[:i] + "I" + string[i:]
            return new_string

    return string
