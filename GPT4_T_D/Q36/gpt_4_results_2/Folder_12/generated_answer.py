
def filter_chars(input_str):
    chars_to_remove = set()
    for char in input_str[33:84]:
        if 'm' < char < 'w':
            chars_to_remove.add(char)
    output_str = "".join([char for char in input_str if char not in chars_to_remove])
    return output_str
