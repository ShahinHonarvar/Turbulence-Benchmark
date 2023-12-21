
def insert_before_character(string, char):
    new_string = ""
    for i in range(len(string)):
        if string[i] == char:
            new_string += "0" + string[i]
        else:
            new_string += string[i]
    return new_string
