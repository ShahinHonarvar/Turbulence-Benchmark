
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "E":
            new_string += string[:i+1] + "E"
            i += 2

        else:

            new_string += string[i]

    return new_string
