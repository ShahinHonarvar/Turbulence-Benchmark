
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "e":
            new_string += string[:i+1] + "0" + string[i+1:]
        else:
            new_string += string[i]
    return new_string
