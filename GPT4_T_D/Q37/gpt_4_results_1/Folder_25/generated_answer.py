
def filter_chars(input_string):
    chars_31_38 = set(input_string[31:39])
    filtered_chars = [char for char in chars_31_38 if ';' <= char <= 'g']

    for char in filtered_chars:
        input_string = input_string.replace(char,"")
        
    return input_string
