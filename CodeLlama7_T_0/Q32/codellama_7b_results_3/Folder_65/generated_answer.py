
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "6":
            new_string += "9" + string[i+1:]
    return new_string
