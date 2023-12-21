
def insert_before_character(string, char_to_insert):
    new_string = ""
    for i in range(len(string)):
        if string[i] == char_to_insert:
            new_string += char_to_insert + new_string[i+1:]
        else:
            new_string += string[i]
    return new_string
