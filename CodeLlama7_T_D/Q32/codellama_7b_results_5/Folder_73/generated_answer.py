
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == 'R':
            new_string += string[:i+1] + "V"
            new_string += string[i+1:]
    return new_string
