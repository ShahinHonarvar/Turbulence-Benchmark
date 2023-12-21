
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "u":
            new_string += string[:i+1] + "u" + string[i+1:]
    return new_string
