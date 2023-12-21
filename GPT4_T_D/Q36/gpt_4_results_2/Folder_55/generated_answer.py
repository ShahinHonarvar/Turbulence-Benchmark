
def filter_chars(input_string):
    chars_to_filter = [ch for ch in input_string[4:5] if 'Y' < ch < 's']
    for ch in chars_to_filter:
        input_string = input_string.replace(ch, "")
    return input_string
