
def filter_chars(input_string):
    char_list = [char for char in input_string[222:419] if char > '-' and char < 'v']
    for char in char_list:
        input_string = input_string.replace(char, '')
    return input_string
