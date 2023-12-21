
def insert_after_character(input_string):
    output_string = ""
    for char in input_string:
        if char == '5':
            output_string += '5h'
        else:
            output_string += char
    return output_string
