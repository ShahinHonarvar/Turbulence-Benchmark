
def filter_chars(input_string):
    filtered_chars = [char for char in input_string[83:93] if '!' < char < '*']
    output_string = ''.join(char for char in input_string if char not in filtered_chars)
    return output_string
