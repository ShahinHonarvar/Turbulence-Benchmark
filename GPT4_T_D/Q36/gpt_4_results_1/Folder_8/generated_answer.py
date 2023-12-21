
def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[83:93] if '!' < char < '*']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string
