
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "6":
            new_string += string[:i+1] + "W"
        else:
            new_string += string[i]
    return new_string
