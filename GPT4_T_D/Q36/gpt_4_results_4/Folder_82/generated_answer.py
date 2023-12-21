
def filter_chars(input_string):
    filtered_string = ""
    for char in input_string[70:97]:
        if 'V' < char < 'j':
            input_string = input_string.replace(char, "")
    return input_string
