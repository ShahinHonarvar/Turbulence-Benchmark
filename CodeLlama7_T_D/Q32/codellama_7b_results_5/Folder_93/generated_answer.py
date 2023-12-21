
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "Y":
            new_string += string[:i+1] + "4"
            string = string[i+1:]
    new_string += string

    return new_string
