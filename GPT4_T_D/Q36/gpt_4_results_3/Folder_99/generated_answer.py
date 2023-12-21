
def filter_chars(input_string):
    target_chars = [char for char in input_string[477:948] if 'b' < char < 'd']
    for char in target_chars:
        input_string = input_string.replace(char, '')
    return input_string
