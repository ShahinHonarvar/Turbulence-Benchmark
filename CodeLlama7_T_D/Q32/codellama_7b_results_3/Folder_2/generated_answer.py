
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "C":
            new_string += string[i:i+1] + "Z"
        else:
            new_string += string[i:i+1]
    return new_string
