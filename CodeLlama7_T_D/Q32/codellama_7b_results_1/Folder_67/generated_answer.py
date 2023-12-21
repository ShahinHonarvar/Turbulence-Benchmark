
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "j":
            new_string += string[:i + 1] + "1"
            i += 1
        else:
            new_string += string[i]
    return new_string
