
def insert_after_character(input_string):
    output_string = ""
    for char in input_string:
        if char == 'H':
            output_string += char + 'n'
        else:
            output_string += char
    return output_string
