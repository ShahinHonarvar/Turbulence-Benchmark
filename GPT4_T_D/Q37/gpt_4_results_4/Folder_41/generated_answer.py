
def filter_chars(input_string):
    filtered_chars = [ch for index, ch in enumerate(input_string[26:65]) if ch < 'V' or ch > 'o']
    for ch in filtered_chars:
        input_string = input_string.replace(ch, '')
    return input_string
