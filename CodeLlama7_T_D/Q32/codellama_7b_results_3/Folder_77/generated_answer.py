
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "9":
            new_string += string[:i+1] + "h" + string[i+1:]
        else:
            new_string += char

    return new_string
