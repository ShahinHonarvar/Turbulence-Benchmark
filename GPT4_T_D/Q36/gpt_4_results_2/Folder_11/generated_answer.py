
def filter_chars(input_string):
    selected_chars = [char for char in input_string[87:93] if char > 'E' and char < '~']
    
    for char in selected_chars:
        input_string = input_string.replace(char, '')
    return input_string
