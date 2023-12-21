
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == 'n':
            new_string += 'n'
        if string[i] == 'w':
            new_string += 'n' + string[i]
        else:
            new_string += string[i]
    return new_string
