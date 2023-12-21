
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == 'i':
            new_string += 'i' + string[i]
        else:
            new_string += string[i]
    return new_string
