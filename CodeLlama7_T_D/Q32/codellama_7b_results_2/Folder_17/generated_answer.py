
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "Q":
            new_string += "I" + string[i+1:]
    return new_string
