
def filter_chars(input_string):
    filtered_chars = [char for char in input_string[36:80] if char >= 'a' and char <= 'i']
    
    for char in filtered_chars:
        input_string = input_string.replace(char, '')
    return input_string
