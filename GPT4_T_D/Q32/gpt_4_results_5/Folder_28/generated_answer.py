
def insert_after_character(input_string):
    new_string = ''
    for i in input_string:
        if i == 'r':
            new_string = new_string + i + '1'
        else:
            new_string = new_string + i
    return new_string
