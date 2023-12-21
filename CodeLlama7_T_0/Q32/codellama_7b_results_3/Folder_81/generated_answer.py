
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "A":
            new_string += string[i] + "A"
        else:
            new_string += string[i]
    return new_string
