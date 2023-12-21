
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "Y":
            new_string += string[:i+1] + "4"
            i += 1
        else:
            new_string += string[i]
    return new_string
