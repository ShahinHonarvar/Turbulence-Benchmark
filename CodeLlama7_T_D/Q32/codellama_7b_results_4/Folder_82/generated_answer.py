
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == 'I':
            new_string += string[:i + 1] + "I"
            i += len("I") - 1
        else:
            new_string += string[i]
    return new_string
