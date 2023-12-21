
def insert_after_character(input_string):
    output_string = ""
    for character in input_string:
        if character == 'R':
            output_string += character + 'V'
        else:
            output_string += character
    return output_string
